from fastapi import FastAPI

app = FastAPI()

#path parameters
@app.get('/user')
def getUser():
    return[
        {
            "name":"lipsa",
            "age":20
        },
        {
            "name":"subhasri",
            "age":20
        },
        {
            "name":"subhasri sabat",
        }
    ]
@app.get('/users')
def getUsers():
    return [
        {
            "name":"subhasri sabat",
            "age":20
        }
    ]