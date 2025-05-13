import psycopg2
import psycopg2.extras
from fastapi import HTTPException
from os import getenv
from dotenv import load_dotenv
import models
from encryption import encode_token, decode_token, hash_password, verify_password

# Connection
def connect():
    """Creates de connection for the database. No parameters needed. Returns the connection."""
    load_dotenv() # Loads the dotenv file

    # Gets the variables for dotenv.
    host = getenv("DATABASE_HOST")
    port = getenv("DATABASE_PORT")
    database = getenv("DATABASE_NAME")
    user = getenv("DATABASE_USER")
    password = getenv("DATABASE_PASSWORD")
    try:
        connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
        )
        return connection
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Can't connect to database: {ex}")

def getCursor(connection):
    """Returns the cursor object. Recieves the parameter \"connection\"."""
    try:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cursor
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Can't create cursor: {ex}")

# User side.

def get_user(user: models.GetUser, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
        query = cursor.fetchone()
        return models.UserClass(**dict(query))
    except Exception as ex:
        raise HTTPException(status_code=404, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()

def create_user(user: models.CreateUser, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (user.username, user.email, hash_password(user.password) ))
        connection.commit()
        return user
    except psycopg2.IntegrityError:
        raise HTTPException(status_code=409, detail="User already exists.")
    except psycopg2.DataError:
        raise HTTPException(status_code=400, detail="Invalid data format.")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()

def delete_user(user: models.UserBase, connection):
    query = get_user(models.GetUser(username=user.username), connection)
    if query:
        if verify_password(user.password, query.password):
            cursor = getCursor(connection)
            try:
                cursor.execute("DELETE FROM users WHERE id=%s", (query.id,))
                connection.commit()
                return "User deleted successfully."
            except Exception as ex:
                raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
            finally:
                cursor.close()
        else:
            raise HTTPException(status_code=401, detail="Incorrect password.")
    else:
        raise HTTPException(status_code=404, detail="No such user.")

def update_user(user: models.UpdateUser, connection):
    query = get_user(models.GetUser(username=user.username), connection)
    if query:
        if verify_password(user.old_password, query.password):
            cursor = getCursor(connection)
            try:
                cursor.execute("UPDATE users SET password=%s WHERE username=%s", (hash_password(user.new_password), user.username))
                connection.commit()
                return "User updated successfully."
            except Exception as ex:
                raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
            finally:
                cursor.close()
        else:
            raise HTTPException(status_code=401, detail="Incorrect password.")
    else:
        raise HTTPException(status_code=404, detail="No such user.")
    

# Pumps side.

def get_pump(pump: models.GetPump, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("SELECT * FROM pumps WHERE id=%s",(pump.id,))
        query = cursor.fetchone()
        return query
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()

def rename_pump(pump: models.RenamePump, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("UPDATE pumps SET name=%s WHERE id=%s",(pump.name, pump.id))
        connection.commit()
        return "Pump renamed successfully."
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()


def get_pumps(connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("SELECT * FROM pumps ORDER BY id ASC")
        pumps = cursor.fetchall()
        return pumps
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()

def create_pump(pump: models.CreatePump, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("INSERT INTO pumps (name, ubication, min_voltage, max_voltage, min_elec_current, max_elec_current, min_flow, max_flow) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (pump.name, pump.ubication, pump.min_voltage, pump.max_voltage, pump.min_elec_current, pump.max_elec_current, pump.min_flow, pump.max_flow))
        connection.commit()
        return pump
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()

def alter_pump(pump: models.GetPump, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("SELECT state FROM pumps WHERE id=%s",(pump.id,))
        pump_state = cursor.fetchone()
        if pump_state:
            cursor.execute("UPDATE pumps SET state=%s WHERE id=%s", (not pump_state[0], pump.id))
            connection.commit()
            return f"Pump alter successfull, now: {not pump_state[0]}"
        else:
            raise HTTPException(status_code=400, detail="No such pump.")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error. {ex}")
    finally:
        cursor.close()

def delete_pump(pump: models.GetPump, connection):
    cursor = getCursor(connection)
    try:
        cursor.execute("DELETE FROM pumps WHERE id=%s", (pump.id,))
        connection.commit()
        return "Pump deleted successfully."
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error. {ex}")
    finally:
        cursor.close()

def update_pump(pump: models.BasePump, connection):
    cursor = getCursor(connection)
    try:
        print(pump)
        cursor.execute("UPDATE pumps SET name=%s, ubication=%s, min_voltage=%s, max_voltage=%s, min_elec_current=%s, max_elec_current=%s, min_flow=%s, max_flow=%s WHERE id=%s", (pump.name, pump.ubication, pump.min_voltage, pump.max_voltage, pump.min_elec_current, pump.max_elec_current, pump.min_flow, pump.max_flow, pump.id))
        connection.commit()
        return "Pump updated successfully."
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Unexpected error. {ex}")
    finally:
        cursor.close()