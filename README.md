# IOTAP-Controller
Sensor-controller implementation

There are 3 dummy functions mocking real sensors. Each controller 
instance = one docker container. Idea is to run in cycle mocking functions
and pass data to MQTT broker. The only argument we should pass to container is
name of sensor, i.e.
ENTRYPOINT ["python3.6","./controller.py"]

docker run --rm <yourImageName> <args>
