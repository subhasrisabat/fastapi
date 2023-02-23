from fastapi import FastAPI
app = FastAPI()
fake_items_db:list =  [{"item_name":"lipstick"},{"items_name":"dress"}]
@app.get('/user/')
def showUser(skip:int = 0, limit:int = 10):
    return fake_items_db[skip:skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id:str,q:str|None =None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item-id":item_id} 