from fastapi import FastAPI, Depends, HTTPException
import models
import database
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from encryption import encode_token, decode_token, verify_password, hash_password
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

connection = database.connect()

# Creates the origins, in this case, the Vue port.
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
# Includes the middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    form_data = models.UserBase(username = form_data.username, password= form_data.password)
    user = database.get_user(form_data, connection)
    if user:
        if verify_password(form_data.password, user.password):
            token = encode_token(user)
            return token
        else:
            raise HTTPException(status_code=401, detail="Incorrect password.")
    else:
        raise HTTPException(status_code=404, detail="No such user.")


@app.put("/new_user")
def create_user(user: models.CreateUser):
    return database.create_user(user, connection)

@app.get("/user")
def user(user: Annotated[models.UserClass, Depends(decode_token)]):
    return user

@app.post("/user")
def update_user(user: models.UpdateUser):
    return database.update_user(user, connection)

@app.delete("/delete")
def delete_user(user: models.UserBase):
    return database.delete_user(user, connection)

@app.post("/pump/{id}")
def get_pump(id):
    return database.get_pump(models.GetPump(id=id), connection)

@app.get("/pumps")
def get_pumps():
    return database.get_pumps(connection)

@app.put("/pumps")
def create_pump(pump: models.CreatePump):
    return database.create_pump(pump, connection)

@app.post("/pumps/alter")
def alter_pump(pump: models.GetPump):
    return database.alter_pump(pump, connection)

@app.delete("/pumps/{id}")
def delete_pump(id: int):
    return database.delete_pump(models.GetPump(id=id), connection)

@app.post("/pumps")
def update_pump(pump: models.BasePump):
    return database.update_pump(pump, connection)

@app.post("/pumps/rename")
def rename_pump(pump: models.RenamePump):
    return database.rename_pump(pump, connection)
