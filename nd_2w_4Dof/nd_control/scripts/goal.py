#! /usr/bin/env python

import os
import time

while True:
    def veri():
        a = os.stat("/home/oguz/mybot_ws/src/nd_control/scripts/goal.txt").st_size
        if (a == 0) :
            print("dosya")
        return a
        
    time.sleep(2)
    b = veri()
    if b == 0 :

        print("konum alinamadi!!!")

    else:
        time.sleep(3)
        file = open("/home/oguz/mybot_ws/src/nd_control/scripts/goal.txt","r")
        liste = file.read()
        file.close()
        print(liste)
        g = liste.split(",")
        g1 = float(g[0])
        g2 = float(g[1])
        g3 = float(g[2])
        g4 = float(g[3])
        print (g1,g2,g3,g4)
        file = open("/home/oguz/mybot_ws/src/nd_control/scripts/goal.txt","w")
