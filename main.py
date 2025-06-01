from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"})

@app.get("/name")
def get_name():
    return JSONResponse(content={"name": "varhsu"})