from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {
        "Success": True,
        "Message": "API is working properly"
    }


@app.get('/v1/hello')
def hello():
    return {
        "Success": True,
        "Message": "Hello, World!"
    }

@app.get('/v1/hello/{name}')
def hello(name: str):
    return {
        "Success": True,
        "Message": f"Hello, {name}!"
    }