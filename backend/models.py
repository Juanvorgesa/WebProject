from pydantic import BaseModel

# General classes.

class PumpClass(BaseModel):
    id: int
    name: str
    ubication: str
    min_voltage: float
    max_voltage: float
    min_elec_current: float
    max_elec_current: float
    min_flow: float
    max_flow: float
    state: bool = False

class UserClass(BaseModel):
    id: int
    email: str
    username: str
    password: str

# Create classes.

class CreateUser(BaseModel):
    username: str
    email: str
    password: str

class CreatePump(BaseModel):
    name: str
    ubication: str
    min_voltage: float
    max_voltage: float
    min_elec_current: float
    max_elec_current: float
    min_flow: float
    max_flow: float


# Query classes.

class GetUser(BaseModel):
    username: str

class GetPump(BaseModel):
    id: int

# Base classes.

class UserBase(BaseModel):
    username: str
    password: str

class BasePump(BaseModel):
    id: int
    name: str
    ubication: str
    min_voltage: float
    max_voltage: float
    min_elec_current: float
    max_elec_current: float
    min_flow: float
    max_flow: float

# Update class.

class UpdateUser(BaseModel):
    username: str
    old_password: str
    new_password: str

class RenamePump(BaseModel):
    id: int
    name: str
