import threading
import queue
from pwdconsumer import PwdConsumer
from pwdproducer import PwdProducer

queue = queue.Queue(maxsize=10)
condition = threading.Condition()


producer = PwdProducer(queue, condition)
consumer1 = PwdConsumer(queue, condition)

producer.start()
consumer1.start()

producer.join()
consumer1.join()
