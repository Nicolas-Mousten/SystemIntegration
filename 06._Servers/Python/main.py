from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "message" : "Welcome to our first server." }

@app.get("/firstroute")
def _():
    return { "message" : "Welcome to the first route, now leave" }

 
