import threading
import time
import random
import queue
sema = threading.Semaphore()
class Producer:
    def __init__(self):
        self.product = ['Haselnuss', 'Schnitzelbroetchen', 'Senf']

    def run(self):
        global q
        while True:
            sema.acquire()
            #Random Produktionszeit(0-3 sekunden)
            time.sleep(random.random()*3)
            f = self.product[random.randrange(len(self.product))]
            q.put(f)
            print("Added: {}".format(f))
            sema.release()
            time.sleep(0.1)


class Consumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global q
        while True:

            sema.acquire()
            #Random Cosumzeit(0-2 Sekunden)
            print('Queue size: {}'.format(q.qsize()))
            if (not q.empty()):
                f = q.get()
                print("Remove: {}".format(f))
                time.sleep(random.random()*2)

            else:
                print('Consumer is waiting for product!')
            sema.release()
            time.sleep(0.1)
            


if __name__ == '__main__':
    q = queue.Queue(10)
    p = Producer()
    c = Consumer()
    pt = threading.Thread(target=p.run, args = ())
    ct = threading.Thread(target=c.run, args = ())
    pt.start()
    ct.start()



