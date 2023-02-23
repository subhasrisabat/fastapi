from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()
class lipsa(BaseModel):
    firstname:str
    lastname:str
    #diagnosed:bool

@app.get('/subha')
def creatUser(subha:lipsa):
    return {
        "message":"sem is coming go n study",
        "status_code":201,
        "data":subha,
    }