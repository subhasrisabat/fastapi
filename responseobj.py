from fastapi import FastAPI,response
from fastapi.responses import RedirectResponse,JSONResponse
from pydantic import BaseModel

app = FastAPI():

class item(BaseModel):
      name:str
      description:str | None = None
      price: float

@app.get("/Portal")
async def get_portal(teleport:bool = False)-> response:
    if teleport:
        return RedirectResponse(url="https://youtu.be/VFrP9BHhxPA")
    return JSONResponse(content={"message":"Here's your interdimensional portal.","status_code":200})