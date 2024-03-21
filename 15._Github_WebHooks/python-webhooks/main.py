from fastapi import FastAPI, Request, Response
import json

app = FastAPI()

@app.post("/githubwebhookjson")
async def github_webhook(request: Request):
    data = await request.body()
    print("Received data:", data.decode())  # Print the raw data received
    try:
        payload = json.loads(data)
        print("Parsed JSON:", payload)  # Print the parsed JSON payload
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    
    print("Hello")
    return 


app.post("/githubwebhookform")
async def github_webhook(request: Request, response: Response):
    if request.headers.get("content-type") == "application/x-www-form-urlencoded":
        form_data = await request.form()
        payload = form_data["payload"]
        print(form_data)

        response.status_code=200
    else:
        response.status_code=400

    return
