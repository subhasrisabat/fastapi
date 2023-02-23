from fastapi import FastAPI,Query,Path,Body
from pydantic import BaseModel

class Mix(BaseModel):
      name:str
      age:int
      job:str

app = FastAPI()

@app.get('/get')
def getMixPath():
    return{
           "message":"mai aapni fav hu"
        }

#body params
@app.post('/body')
def PostMix(data:Mix):
      return{
            "data":data
      }

