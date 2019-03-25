import threading
import queue
import numpy as np
from password import Password



class PwdProducer(threading.Thread):
    def __init__(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition
    def run(self):
        while True:
            password = input("Next Password: ")
            self.condition.acquire()
            try:
                self.queue.put(Password(password), block = False)
                self.condition.notify()
            except queue.Full:
                self.condition.wait()
            self.condition.release()


