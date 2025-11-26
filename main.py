from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from functions import sort_csv
app = FastAPI()


@app.post ("/assignWithCsv")
async def create_file(file: Annotated[bytes, File()]):
    sort_csv(file)
    
    # new_text = kesar(text.text,text.offset,text.mode)
    # return {"msg":new_text}





# @app.get ("/test")
# def read_tesr():
#     return {"msg": "hi from test"}

# @app.get ("/test/name")
# def saved_user(name):
#     with open("user.txt","a") as f:
#         f.write(f"{name} ")
#     return {"msg": "Hello","name":name}

# @app.post ("/caesar")
# def caesar_cipher(text:Encrypting):
#     new_text = kesar(text.text,text.offset,text.mode)
#     return {"msg":new_text}

# @app.get (" /fence/encrypt/{text}")
# def gader()