import mocks.sensor_mock as sensor_mock
import yaml

import paho.mqtt.client as mqtt
from controller import Controller

def run_controller(sensor):
    callback = getattr(sensor_mock, sensor["port"])
    callback()
    controller = Controller(name=sensor['name'])
    controller.start()

if __name__ == "__main__":
    with open("controllers.conf.yml") as conf: #TODO Check exception throwing
        config = yaml.full_load(conf)
    if config is None:
        print("controllers.conf.yml is not found")

    #TODO Validate conf file

    [run_controller(sensor) for sensor in config['sensors']]



    # broker_address = "127.0.0.1"

    # client = mqtt.Client("P1")  # create new instance
    # client.connect(broker_address)  # connect to broker
    # client.publish("house/main-light", "OFF")  # publish
    # client.disconnect()


