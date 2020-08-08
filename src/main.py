import yaml
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mocks import sensor_mock

from controller import Controller

def run_controller(sensor):
    callback = getattr(sensor_mock, sensor["port"])
    callback()
    controller = Controller(name=sensor['name'])
    controller.start()

if __name__ == "__main__":
    print ("Controller is started")
    with open("configs/controller.conf.yml") as conf: #TODO Check exception throwing
        config = yaml.full_load(conf)
    if config is None:
        print("controller.conf.yml is not found")

    #TODO Validate conf file

    [run_controller(sensor) for sensor in config['sensors']]



    # broker_address = "127.0.0.1"

    # client = mqtt.Client("P1")  # create new instance
    # client.connect(broker_address)  # connect to broker
    # client.publish("house/main-light", "OFF")  # publish
    # client.disconnect()


