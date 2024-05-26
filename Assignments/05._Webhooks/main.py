from fastapi import FastAPI, HTTPException, Request
import json
import requests
app = FastAPI()
webhooks: dict[str, str] = {}


@app.post("/registerWebhook/{event_type}")
async def subscribe(event_type: str, request: Request):
    payload = await request.json()
    url = payload.get("url")

    webhooks[event_type] = url
    print(event_type, url)
    return {"message": f"Webhook registered for event type: {event_type}"}
    

@app.delete("/unregisterWebhook/{event_type}")
def unsubscribe(event_type: str):
    if event_type in webhooks:
        del webhooks[event_type]
        return {"message": f"Webhook unregistered for event type: {event_type}"}
    else:
        raise HTTPException(status_code=404, detail="Webhook not found")


@app.post("/ping")
def ping_webhooks():
    results = []
    for event_type, callback_url in webhooks.items():
        payload = {"event_type": event_type, "message": "Ping!"}
        response = requests.post(callback_url, json=payload)
        if response.status_code == 200:
            results.append({"event_type": event_type, "status": "Success", "data": callback_url})
        else:
            results.append({"event_type": event_type, "status": "Failed", "error": response.text})
    
    return {"results": results}

@app.post("/test")
def _():
    return {"message": "Hello There"}