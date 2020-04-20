import threading
import time
import random
import queue

class Producer1:
    def __init__(self):
        self.product = ['Senf']

    def run(self):
        global q1
        while True:
            sema1.acquire()
            #Random Produktionszeit(0-3 sekunden)
            time.sleep(random.random()*3)
            f = self.product[random.randrange(len(self.product))]
            q1.put(f)
            print("Added: {}".format(f))
            sema1.release()
            time.sleep(0.1)

class Producer2:
    def __init__(self):
        self.product = ['Haselnuss']

    def run(self):
        global q2
        while True:
            sema2.acquire()
            #Random Produktionszeit(0-3 sekunden)
            time.sleep(random.random()*3)
            f = self.product[random.randrange(len(self.product))]
            q2.put(f)
            print("Added: {}".format(f))
            sema2.release()
            time.sleep(0.1)


class Consumer1:
    def __init__(self):
        self.next = 0

    def run(self):
        global q1
        global q2
        while True:
            sema1.acquire()
            print('Queue1 size: {}'.format(q1.qsize()))
            if (not q1.empty()):
                f = q1.get()
                print("Remove: {}".format(f))
                time.sleep(random.random()*1)
            else:
                print('Consumer is waiting for product!')
            sema2.acquire()
            #Random Cosumzeit(0-2 Sekunden)
            print('Queue2 size: {}'.format(q2.qsize()))
            if (not q2.empty()):
                f = q2.get()
                print("Remove: {}".format(f))
                time.sleep(random.random()*1)
            else:
                print('Consumer is waiting for product!')
            sema1.release()
            sema2.release()
            time.sleep(0.1)

class Consumer2:
    def __init__(self):
        self.next = 0

    def run(self):
        global q1
        global q2
        while True:
            sema1.acquire()
            print('Queue1 size: {}'.format(q1.qsize()))
            if (not q1.empty()):
                f = q1.get()
                print("Remove: {}".format(f))
                time.sleep(random.random()*1)
            else:
                print('Consumer is waiting for product!')
            sema2.acquire()
            #Random Cosumzeit(0-2 Sekunden)
            print('Queue2 size: {}'.format(q2.qsize()))
            if (not q2.empty()):
                f = q2.get()
                print("Remove: {}".format(f))
                time.sleep(random.random()*1)
            else:
                print('Consumer is waiting for product!')
            sema1.release()
            sema2.release()
            time.sleep(0.1)


if __name__ == '__main__':
    sema1 = threading.Semaphore()
    sema2 = threading.Semaphore()
    q1 = queue.Queue(10)
    q2 = queue.Queue(10)
    p1 = Producer1()
    p2 = Producer2()
    c1 = Consumer1()
    c2 = Consumer2()
    pt1 = threading.Thread(target=p1.run, args = ())
    pt2 = threading.Thread(target=p2.run, args = ())
    ct1 = threading.Thread(target=c1.run, args = ())
    ct2 = threading.Thread(target=c2.run, args = ())
    pt1.start()
    pt2.start()
    ct1.start()
    ct2.start()



