from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#this is a secret model
class PackageIn(BaseModel):
    secret_id:int
    name:str
    number:str
    description:Optional[str] = None

#this is like a public model
class Package(BaseModel):
    name:str
    number:str
    description:Optional[str] = None


app=FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello":"World"}



# @app.get('/component/{component_id}') #path parameter
# async def get_component(component_id):
#     return {"component_id":component_id}

# @app.get('/component/')
# async def read_component(number:int,text:Optional[str]): #query parameter
#     return {"number":number,"text":text}

# @app.post('/package/{priority}')
# async def make_package(priority:int,package:Package,value : bool):
#     return {"priority":priority, **package.dict(), "value":value}

#response_model_include={"description"}  displays only description and not others .....exclude will displayother thanthe specified ones.
#when response_model_exclude_unset=true....we can just pass the values that doesnt have default ones and still get the response correctly
@app.post('/package/',response_model=Package,response_model_exclude_unset=True)#the response model is what customer needs to display
async def make_package(package:PackageIn):#packageIn contains confidential inputs and info...soo we use a seperate model for response
    return package