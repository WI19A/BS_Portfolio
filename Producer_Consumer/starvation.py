from threading import Thread
import time

cedric = 0
markus = 0
#Implementiert eine Methode
def Producer(x):
    #System Out
    print("Start Thread%s" % x)
    cedric1 = 0
    for _ in range(10):
        global cedric
        cedric1 = cedric1 + 1
        cedric = cedric1
        print("prod",cedric)
    print("Stop Thread%s" % x)
    

def Consumer(x):
    #System Out
    print("Start Thread%s" % x)
    for _ in range(10):
        global cedric
        global markus
        while cedric == 0:
            time.sleep(0.1)
        markus = markus+ cedric
        cedric = 0
        print("cons",markus)
    print("Stop Thread%s" % x)




#Methodenaufruf
t=Thread(target=Producer, args=("Producer", ))
t.start()
time.sleep(0.1)
t=Thread(target=Consumer, args=("Consumer", ))
t.start()



