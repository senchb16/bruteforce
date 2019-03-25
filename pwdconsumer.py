import threading
import queue
import itertools
import string


class PwdConsumer(threading.Thread):

    def __init__(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while True:
            password = None
            self.condition.acquire()
            try:
                password = self.queue.get(False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            # todo brute force algorithm
            istrue = False
            if not password is None:
                letters = string.ascii_letters + string.digits + string.punctuation
                print(letters)
                for i in range(1, 31):
                    for j in map(''.join, itertools.product(letters, repeat=i)):
                        print("Password: "+j)
                        if password.check(j):
                            print("Password found: "+j)
                            istrue = True
                            break
                    if(istrue):
                        break








