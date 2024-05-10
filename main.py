from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"message": "Hello, World! This is my Python API running on Azure App Service with FastAPI."}
