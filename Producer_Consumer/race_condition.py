from threading import Thread
import time

cedric = 0
#Implementiert eine Methode
def Producer(x):
    #System Out
    #print("Start Thread%s" % x)
    for _ in range(100000):
        inc()
    #print("Stop Thread%s" % x)

def Consumer(x):
    global cedric
    print(cedric)
    
def inc():
    global cedric
    cedric += 1



#Methodenaufruf
def start():
    global cedric
    cedric = 0
    t1=Thread(target=Producer, args=("Producer1", ))
    t2=Thread(target=Producer, args=("Producer2", ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    t3=Thread(target=Consumer, args=("Consumer", ))
    t3.start()

    

for i in range(10):
    start()
    #print("Iteration",i, cedric)