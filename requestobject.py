from fastapi import FastAPI,request
from pydantic import BaseModel

class subha(BaseModel):
      name:str;
      age:20;

app = FastAPI()
@app.post('/')
def showBody(req:request):
    return{
        "baseURL":req.base_url,
        "method":req.method,
        "host":req.headers
    }
