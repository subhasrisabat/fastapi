from fastapi import FastAPI,Query

app = FastAPI()

@app.get('/')
def homepage():
    return{
        "homepage"
    }
#query params validation
@app.get('/subha/')
def subha_validation(nationality:str):
    results ={"data":[{"name":'subhasri sabat'},{"age":20}]}
    if nationality:
         results.update({"nationlity":nationality})
         return results  

@app.get('/subhasri/')
def subha_validation(shidhart_molhotra: str |None = Query(default= None,min_length=10,max_length=5)):
    results = {"data":[{"manish_molhotra":"indian fasion designer"}]}
    if shidhart_molhotra:
        results.update({"new groom":shidhart_molhotra})
    return results

from fastapi import FastAPI,Query
from pydantic import Required
@app.get('/subu/')
def subha_validation(shidhart_molhotra: str |None = Query(default= Required,min_length=10,max_length=5)):
    results = {"data":[{"manish_molhotra1":"indian fasion designer"},
                       {"manish_molhotra2":"56 years old"}]}
    if shidhart_molhotra:
        results.update({"new groom":shidhart_molhotra})
    return results