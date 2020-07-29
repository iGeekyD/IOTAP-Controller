from mocks.sensor_mock import generate_temperature

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


if __name__ == "__main__":

    broker_address = "127.0.0.1"

    client = mqtt.Client("P1")  # create new instance
    client.connect(broker_address)  # connect to broker
    client.publish("house/main-light", "OFF")  # publish
    client.disconnect()


