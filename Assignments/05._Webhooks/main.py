from fastapi import FastAPI, Request, Response
import json

app = FastAPI()

@app.post("/WebhookTest")
async def webhook_test(request: Request):
    data = await request.body()
    print("Received data:", data.decode())  # Print the raw data received
    try:
        payload = json.loads(data)
        print("Parsed JSON:", payload)  # Print the parsed JSON payload
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    
    print("Hello")
    return 