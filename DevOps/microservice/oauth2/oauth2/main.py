from fastapi import FastAPI
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret Key"

def create_access_token(subject:str, expires_delta:timedelta):
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.get("/new_route")
def get_access_token(user_name: str):
    """
    Understanding the access token
    -> Takes user_name as input and returns access token
    -> timedelta(minutes=1) is used to set the expiry time of the access token to 1 minute
    """
    
    access_token_expires = timedelta(minutes=1)
    access_token = create_access_token(subject=user_name, expires_delta=access_token_expires)
    
    return {"access_token": access_token}

@app.get("/")
def read_root():
    return {"Hello": "I am updating"}

