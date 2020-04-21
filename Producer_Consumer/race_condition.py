import threading
import time
import random


index = 0
q = [None]*10

class Producer(threading.Thread): #Producer erbt von Thread
    def __init__(self, iD, name):   
        threading.Thread.__init__(self) #super Constructer
        self.product = ['Haselnuss', 'Schnitzelbroetchen', 'Senf']
        self.iD = iD
        self.name = name

    def run(self):
        global q
        global index
        while index < 9:
            #Random Produktionszeit(0-3 sekunden)
            time.sleep(1) #Kein Random Sleep, um raceCondition zu zeigen(Threads muessen gleichzeitig was veraendern)
            f = self.product[random.randrange(len(self.product))]
            q[index]=f
            print("Thread{1} Added: {0} on {2}".format(f, self.iD, index))
            index+=1
            
class Consumer(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name

    def run(self):
        global q
        #while True:
            #if (len(q)>9):
            #Random Cosumzeit(0-2 Sekunden)
      
if __name__ == '__main__':
    #Threadstart
    p1 = Producer(1,"Prod1")
    p2 = Producer(2,"Prod2")

    #c1 = Consumer(1,"Cons1")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(q)
    #c1.start()