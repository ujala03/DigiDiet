import paho.mqtt.client as mqtt
import pandas as pd
import json
import ssl
import time

# 🔹 AWS IoT Core Configuration
AWS_IOT_ENDPOINT = "a34at8uvmnf6hp-ats.iot.ap-southeast-2.amazonaws.com"
THING_NAME = "digi-diet4"
TOPIC = "abcd"

CERTIFICATE_PATH = r"C:\Users\DELL\Downloads\5fd75ed30445a53e00ca24ced9e937c6555e1ef1ad0bdfc8562fc260c3ceef9c-certificate.pem.crt"
PRIVATE_KEY_PATH = r"C:\Users\DELL\Downloads\5fd75ed30445a53e00ca24ced9e937c6555e1ef1ad0bdfc8562fc260c3ceef9c-private.pem.key"
ROOT_CA_PATH = r"C:\Users\DELL\Downloads\AmazonRootCA1 (3).pem"
EXCEL_FILE_PATH = r"C:\Users\DELL\OneDrive\Desktop\digi-diet-final.xlsx" # Update with your Excel file

# 🔹 MQTT Client Setup
client = mqtt.Client(client_id=THING_NAME)
client.tls_set(
    ca_certs=ROOT_CA_PATH, 
    certfile=CERTIFICATE_PATH, 
    keyfile=PRIVATE_KEY_PATH, 
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# 🔹 MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to AWS IoT Core")
    else:
        print(f"⚠ Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"📤 Message {mid} published successfully.")

client.on_connect = on_connect
client.on_publish = on_publish

# 🔹 Connect to AWS IoT Core
client.connect(AWS_IOT_ENDPOINT, 8883, 60)
client.loop_start()

# 🔹 Read Excel & Publish Data
def publish_excel_data():
    df = pd.read_excel(EXCEL_FILE_PATH)  # Read Excel file
    
    for _, row in df.iterrows():
        image_link = str(row[0])  # Read first column (assuming it contains links)
        
        if pd.isna(image_link):  
            continue  # Skip empty rows
        
        payload = {"image_link": image_link}
        
        client.publish(TOPIC, json.dumps(payload))
        print(f"📡 Sent: {payload}")
        time.sleep(2)  # Adjust delay if needed

try:
    publish_excel_data()
except KeyboardInterrupt:
    print("🛑 Stopped sending data")

client.disconnect()
client.loop_stop()