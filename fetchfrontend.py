import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"📩 Received from client: {message}")
            
            # Simulated response with an image link
            response = json.dumps({"image_link": "https://example.com/image.jpg"})
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("🔌 Client disconnected")
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handler, "localhost", 5000)
    print("✅ WebSocket Server started on ws://localhost:5000")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())