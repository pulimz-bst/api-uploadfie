import re 
# from main_lib import *   
from fastapi import Depends, FastAPI , HTTPException ,File, UploadFile
from fastapi.param_functions import Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime, timedelta
from typing import Optional 
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import numpy as np  
import base64
import requests

   
# from lib.imageSearch import imageSearch
# from 
# from productSearch import productSearch 

class Urltob64(BaseModel): 
    url : str 

class Example(BaseModel): 
    foldername : str 
    productImage : str = Body(...,example="https://... ") 
 

SECRET_KEY = "21bb28cfdac986bd041470db0ef8cbe32ecf18cfcea96163c6fc37f5ec6e4f89"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  

users_db = {
    "bst-service": {
        "username": "bst-service",
        "full_name": "thebrainstem",
        "email": "service@thebrainstem.com", 
        "hashed_password": "$2b$12$vIMfE/1F7l9PaKvncCkhmORVBygomq/iXJRHFspFkS8eA0hAmI54q",
        "disabled": False,
    }
}

app = FastAPI() 

@app.get("/")
def home(): 
    return {"message":" GET HOME "} 


@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
def read_item_test(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
 
@app.post("/url-to-b64")
async def urltob64(reqest : Urltob64):  
    res = get_as_base64(url=reqest.url)
    return{ 
            'base64': res,   
        }  

@app.post("/example")
async def product_search_api(reqest : Example):  
    try: 
        foldername          =  reqest.foldername
        productImage        =  reqest.productImage 
        return{ 
            'foldername': foldername,  
            'productImage':  productImage  
        }  
    except ValueError as e:
        return{ 
            'error_code':  str(e),  
        } 
 
def get_as_base64(url): 
    return base64.b64encode(requests.get(url).content)


def test():
    print("test")
 

if __name__ == '__main__':
    endpoint = "https://i.stack.imgur.com/N4TSy.jpg"
    res = get_as_base64(url=endpoint)

    print(res)




 
