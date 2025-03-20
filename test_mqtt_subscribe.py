import paho.mqtt.client as mqtt
import ssl

# AWS IoT Core Configuration
AWS_IOT_ENDPOINT = "a34at8uvmnf6hp-ats.iot.ap-southeast-2.amazonaws.com"
TOPIC = "abcd"
THING_NAME = "digi-diet4"

CERTIFICATE_PATH = r"C:\Users\DELL\Downloads\5fd75ed30445a53e00ca24ced9e937c6555e1ef1ad0bdfc8562fc260c3ceef9c-certificate.pem.crt"
PRIVATE_KEY_PATH = r"C:\Users\DELL\Downloads\5fd75ed30445a53e00ca24ced9e937c6555e1ef1ad0bdfc8562fc260c3ceef9c-private.pem.key"
ROOT_CA_PATH = r"C:\Users\DELL\Downloads\AmazonRootCA1 (3).pem"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to AWS IoT Core")
        client.subscribe(TOPIC)
        print(f"📡 Subscribed to topic: {TOPIC}")
    else:
        print(f"⚠ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"📥 Received from MQTT: {msg.payload.decode()}")  # Debugging

def on_subscribe(client, userdata,mid, granted_qos):
    print(f"Successfully Subscribed (QoS {granted_qos})")

# Setup MQTT Client
client = mqtt.Client(client_id=THING_NAME)
client.tls_set(
    ca_certs=ROOT_CA_PATH, 
    certfile=CERTIFICATE_PATH, 
    keyfile=PRIVATE_KEY_PATH, 
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.tls_insecure_set(True)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

# Connect & Listen
client.connect(AWS_IOT_ENDPOINT, 8883, 60)
client.loop_forever()