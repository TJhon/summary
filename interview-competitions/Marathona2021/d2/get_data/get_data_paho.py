import paho.mqtt.client as mqtt
import time as tm
import json

broker = "iot.maratona.dev"
port = 31666
topic = "quanam"
username = "maratoners"
password = "btc-2021"



def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)
    #print(topic)

store = []

def on_message(client, userdata, msg):
    #print("recivido")
    print(msg.topic + " " + str(msg.payload))
    data = json.loads(msg.payload)
    store.append(data)
    #print(str(data))




client = mqtt.Client()
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

client.loop_start()

client.subscribe(topic, 1)

client.user_data_set(1)

client.loop()

tm.sleep(3300)

client.loop_stop(force = True)

print('end')

with open("data_iot.json", "w", encoding="utf-8") as f:
    json.dump(store, f, ensure_ascii=False, indent=4)