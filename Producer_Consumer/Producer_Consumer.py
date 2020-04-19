from threading import Thread
import time

w = 0
cedric = 0
markus = 0
#Implementiert eine Methode
def Producer(x):
    #System Out
    print("Start Thread%s" % x)
    for i in range(10):
        global w
        global cedric
        while w:
            time.sleep(0.1)
        cedric = cedric+1
        print("prod",cedric)
        w =1
    print("Stop Thread%s" % x)
    

def Consumer(x):
    #System Out
    print("Start Thread%s" % x)
    for i in range(10):
        global w
        global markus
        markus = markus+ cedric
        w = 0
        print("cons",markus)
    print("Stop Thread%s" % x)




#Methodenaufruf


t=Thread(target=Producer, args=("Producer", ))
t.start()
time.sleep(1)
t=Thread(target=Consumer, args=("Consumer", ))
t.start()





