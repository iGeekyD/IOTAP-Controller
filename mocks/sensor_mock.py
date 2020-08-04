from random import random, choice

def generate_temperature():
    return random()*14 + 16

def generate_humidity():
    return random()*70 + 30

def generate_movement():
    choice(["ON", "OFF"])