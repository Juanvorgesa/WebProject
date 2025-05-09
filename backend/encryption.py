from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv
from typing import Annotated
from fastapi import Depends
from models import UserClass
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
load_dotenv() # Loads the dotenv variables.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = getenv("SECRET_KEY")
ENCRYPT_ALGORITHM = getenv("ENCRYPT_ALGORITHM")

def encode_token(payload: UserClass) -> str:
    token = jwt.encode(payload.dict(), SECRET_KEY, algorithm=ENCRYPT_ALGORITHM)
    return {
        "access_token": token
    }

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> UserClass:
    user = jwt.decode(token, SECRET_KEY, algorithms=ENCRYPT_ALGORITHM)
    return user

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)