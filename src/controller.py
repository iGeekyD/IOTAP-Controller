from threading import Thread
import time
class Controller(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("I am %s" % self.name)
        time.sleep(3)