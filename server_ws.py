import asyncio
import websockets

async def send_data(websocket, path):
    while True:
        message = "Hello from WebSocket Server!"
        await websocket.send(message)
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(send_data, "localhost", 5000):
        await asyncio.Future()  # Keeps server running

# ✅ Use asyncio.run() to start event loop properly
if __name__ == "__main__":
    asyncio.run(main())
