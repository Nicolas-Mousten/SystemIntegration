from fastapi import FastAPI;
import requests

app = FastAPI()

@app.get("/fastapiData")
def _():
    return { "message" : [1,2,3,4,5] }


@app.get("/requestExpress")
def _():

    url = "http://127.0.0.1:8080/expressData"

    response = requests.get(url).json()

    return { "data" : response } 