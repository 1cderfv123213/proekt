import os
import glob
import shutil
import numpy as np
import time
import json
import random
def zero():
    puti = "D:\\нейронка\\"
    map = []
    t = 49
    mesto = [[], []]
    for j in range(50):#карта нулёвая
        s1 = []
        for i in range(50):
            s1.append(0)
        map.append(s1)
    for g in range(49): #Таракан
            x = random.randint(0, 48)
            y = random.randint(0, 48)
            if map[x][y] == 0:
                mesto[0].append(x)
                mesto[1].append(y)
                map[x][y] = 100
            else:
                while map[x][y] != 0 and t!=1:
                    x = random.randint(0, 48)
                    y = random.randint(0, 48)
                    if map[x][y] == 0:
                        mesto[0].append(x)
                        mesto[1].append(y)
                        map[x][y] = 100
                        t = 1
                t = 0
    for g in range(49):  # еда
        x = random.randint(0, 48)
        y = random.randint(0, 48)
        if map[x][y] == 0:
            map[x][y] = -100
        else:
            while map[x][y] != 0 and t != 1:
                x = random.randint(0, 48)
                y = random.randint(0, 48)
                if map[x][y] == 0:
                    map[x][y] = -100
                    t = 1
            t = 0
    for g in range(49):  # яд
        x = random.randint(0, 48)
        y = random.randint(0, 48)
        if map[x][y] == 0:
            map[x][y] = -200
        else:
            while map[x][y] != 0 and t != 1:
                x = random.randint(0, 48)
                y = random.randint(0, 48)
                if map[x][y] == 0:
                    map[x][y] = -200
                    t = 1
        t = 0
    json.dump(mesto, open(puti + 'mesto.txt', 'w', encoding="UTF-8"))
    json.dump(map, open(puti + 'map.txt', 'w', encoding="UTF-8"))