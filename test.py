#!/usr/bin/python
import logging
import time
from threading import Thread

#Implementiert eine Methode
def test(i):
    #System Out
    print("Start Thread%d" % i)
    #Sleep
    time.sleep(5)
    print("Stop Thread%d" % i)

#Methodenaufruf
for i in range(10):
    t=Thread(target=test, args=(i, ))
    time.sleep(0.2)
    t.start()


