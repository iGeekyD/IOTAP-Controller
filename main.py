from mocks.sensor_mock import generate_temperature

import paho.mqtt.client as mqtt

def run_controller(sensor):
    create_thread()
    Controller.run()

if __name__ == "__main__":
    read_config()

    foreach sensor in sensors:
    run_controller(sensor)

    broker_address = "127.0.0.1"

    client = mqtt.Client("P1")  # create new instance
    client.connect(broker_address)  # connect to broker
    client.publish("house/main-light", "OFF")  # publish
    client.disconnect()


