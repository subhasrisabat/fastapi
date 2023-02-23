from fastapi import FastAPI,Path
from pydantic import Required

app = FastAPI()
#simple path param
@app.get('/{path}')
def pathparam(path):
    print({"path":path})
    return{
        "path":path
    }
    #simple path params with path class
    @app.get('/path/{path}')
    def pathparamwithpath(path:int/None =
                           path(default = None,
                           description= "lipsa sabat",
                           ge=3,
                           le=5,
                           deprecated= True,
                           include_in_schema=True)):
    print({"path":path})
    return{
        "path":path
    }


#simple pathparam with path class and query params with query class
from fastapi import FastAPI,Query,Path
from pydantic import Required
@app.get('/path/query/{path}')
def pathandqueryparam(
           q:str | None = Query(default = Required,description= "subha"),
           path:int |None = Path(default=None,description="crazy girl",ge=2,le=6,deprecated=True,include_in_schema=True)):
        print({"path":path})
        if q:
            return{
                "query":q,
                "path":path
            }