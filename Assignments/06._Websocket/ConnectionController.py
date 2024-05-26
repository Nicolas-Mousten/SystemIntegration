from fastapi import WebSocket

class Controller:
    def __init__(self) -> None:
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user_name: str):
        print("Tried to connect with :", websocket) 
        await websocket.accept()
        if user_name not in self.active_connections:
            self.active_connections[user_name] = []
        self.active_connections[user_name].append(websocket)
    
    def disconnect(self, websocket: WebSocket, user_name: str):
        if user_name in self.active_connections:
            self.active_connections[user_name].remove(websocket)
    
    async def sendMessage(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str, sender_name: str):
        for user_name, connections in self.active_connections.items():
            if user_name != sender_name:
                for connection in connections:
                    await connection.send_text(message)