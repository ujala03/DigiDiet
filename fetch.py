import paho.mqtt.client as mqtt
import json
import ssl
from flask import Flask
from flask_sock import Sock

# 🔹 AWS IoT Core Configuration
AWS_IOT_ENDPOINT = "a34at8uvmnf6hp-ats.iot.ap-southeast-2.amazonaws.com"
THING_NAME = "digi-diet4"
TOPIC = "abcd"

CERTIFICATE_PATH = r"C:\Users\DELL\Downloads\5fd75ed30445a53e00ca24ced9e937c6555e1ef1ad0bdfc8562fc260c3ceef9c-certificate.pem.crt"
PRIVATE_KEY_PATH = r"C:\Users\DELL\Downloads\5fd75ed30445a53e00ca24ced9e937c6555e1ef1ad0bdfc8562fc260c3ceef9c-private.pem.key"
ROOT_CA_PATH = r"C:\Users\DELL\Downloads\AmazonRootCA1 (3).pem"

# 🔹 Flask Setup
app = Flask(__name__)
sock = Sock(app)
clients = []  # Store active WebSocket clients

# 🔹 MQTT Client Setup
mqtt_client = mqtt.Client(client_id=THING_NAME)
mqtt_client.tls_set(
    ca_certs=ROOT_CA_PATH, 
    certfile=CERTIFICATE_PATH, 
    keyfile=PRIVATE_KEY_PATH, 
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# 🔹 MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to AWS IoT Core")
        client.subscribe(TOPIC)  # Subscribe to incoming messages
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"⚠ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print(f"📥 Received from MQTT: {message}")
    
    # Send the message to all connected WebSocket clients
    for ws in clients:
        try:
            ws.send(message)
            print(f"Sent to Websocket Client: {message}")
        except Exception as e:
            print(f"Websocket Send Error: {e}")
            clients.remove(ws)  # Remove disconnected clients

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# 🔹 Connect to AWS IoT Core & Start Listening
mqtt_client.connect(AWS_IOT_ENDPOINT, 8883, 60)
mqtt_client.loop_start()

# 🔹 WebSocket Route (Frontend Connects Here)
@sock.route("/ws")
def websocket(ws):
    clients.append(ws)
    print("🌐 WebSocket Client Connected")
    
    while True:
        try:
            data = ws.receive()  # Keep connection open
        except:
            break
    
    clients.remove(ws)
    print("🔌 WebSocket Client Disconnected")

# 🔹 Start Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)