from threading import Thread
import time
prod1 = 0
prod2 = 0
cedric = 0
justin = 0
markus = 0
simon = 0
#Implementiert eine Methode
def Producer1(x):
    #System Out
    print("Start Thread%s" % x)
    cedric1 = 0
    for i in range(20):
        global cedric
        global prod1
        while prod1 != 0:
            time.sleep(0.1)
        cedric1 = cedric1 + 1
        cedric = cedric1
        prod1 = 1
        print("prod",cedric)
    print("Stop Thread%s" % x)

def Producer2(x):
    #System Out
    print("Start Thread%s" % x)
    cedric2 = 0
    for i in range(20):
        global justin
        global prod2
        while prod2 != 0:
            time.sleep(0.1)
        cedric2 = cedric2 + 1
        justin = cedric2
        prod2 = 1
        print("prod",cedric)
    print("Stop Thread%s" % x)
    

def Consumer1(x):
    #System Out
    print("Start Thread%s" % x)
    for i in range(10):
        global cedric
        global justin
        global markus
        global prod1
        global prod2
        while cedric == 0:
            time.sleep(0.1)
        cedric1 = cedric
        cedric = 0
        time.sleep(0.1)
        while justin == 0:
            time.sleep(0.1)
        justin1 = justin
        justin = 0
        markus = markus + cedric1 + justin1
        prod1 = 0
        prod2 = 0
        print("cons",markus)
    print("Stop Thread%s" % x)

def Consumer2(x):
    #System Out
    print("Start Thread%s" % x)
    for i in range(10):
        global cedric
        global justin
        global simon
        global prod1
        global prod2
        while justin == 0:
            time.sleep(0.1)
        justin1 = justin
        justin = 0
        time.sleep(0.1)
        while cedric == 0:
            time.sleep(0.1)
        cedric1 = cedric
        cedric = 0
        
        simon = simon+ cedric1 + justin1
        prod1 = 0
        prod2 = 0
        print("cons",markus)
    print("Stop Thread%s" % x)




#Methodenaufruf
t=Thread(target=Producer1, args=("Producer1", ))
t.start()
time.sleep(0.1)
t=Thread(target=Producer2, args=("Producer2", ))
t.start()
time.sleep(0.1)
t=Thread(target=Consumer1, args=("Consumer1", ))
t.start()
time.sleep(0.1)
t=Thread(target=Consumer2, args=("Consumer2", ))
t.start()