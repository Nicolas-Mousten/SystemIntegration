from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from ConnectionController import Controller
from fastapi.templating import Jinja2Templates

controller = Controller()

app = FastAPI()
templates = Jinja2Templates(directory="static")

@app.get("/")
def _(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws/{user_name}")
async def _(websocket: WebSocket, user_name: str):
    await controller.connect(websocket, user_name)
    try:
        while True:
            data = await websocket.receive_text()
            await controller.sendMessage(f"{user_name}: {data}", websocket)
            await controller.broadcast(f"{user_name} -> {data}", user_name)
    except WebSocketDisconnect:
        controller.disconnect(websocket, user_name)
        await controller.broadcast(f"{user_name} left the chat", user_name)