from fastapi import FastAPI, WebSocket
import json
import asyncio

app = FastAPI()

# Sample food data
foods = [
    {
        "name": "2 Cup Tea",
        "image": "https://digi-diet-final.s3.eu-north-1.amazonaws.com/2-cup-tea.jpeg",
        "protein": 2,
        "carbohydrate": 30,
        "fat": 3
    },
    {
        "name": "Apple",
        "image": "https://digi-diet-final.s3.eu-north-1.amazonaws.com/apple.jpeg",
        "protein": 0.3,
        "carbohydrate": 25,
        "fat": 0.2
    },
    {
        "name": "Banana",
        "image": "https://digi-diet-final.s3.eu-north-1.amazonaws.com/banana.jpg",
        "protein": 1.3,
        "carbohydrate": 27,
        "fat": 0.3
    },
    {
        "name": "Roti",
        "image": "https://digi-diet-final.s3.eu-north-1.amazonaws.com/roti.jpg",
        "protein": 3,
        "carbohydrate": 18,
        "fat": 1
    },
    {
        "name": "Samosa",
        "image": "https://digi-diet-final.s3.eu-north-1.amazonaws.com/samosa.jpg",
        "protein": 3,
        "carbohydrate": 32,
        "fat": 17
    }
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket Connection Established")

    try:
        while True:
            for food in foods:
                await websocket.send_text(json.dumps(food))
                await asyncio.sleep(5)  # Send a new food item every 5 seconds
    except Exception as e:
        print(f"⚠ WebSocket Error: {e}")
    finally:
        print("🔌 WebSocket Disconnected")
