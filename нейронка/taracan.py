import os
import glob
import shutil
import numpy as np
import time
import json
put = "D:\\нейронка\\"
t = 0
map = json.load(open(put + 'map.txt', 'r'))
mesto = json.load(open(put + 'mesto.txt', 'r'))
puti = "D:\\нейронка\\pamiati\\"
def robot (x):
    global t
    y=str(x)
    del1 = json.load(open(puti + y + '.txt', 'r'))
    st = json.load(open(puti + y + 'str.txt', 'r'))
    hp = json.load(open(puti + y + 'hp.txt', 'r'))
    if st > 58:
        st -= 59
    if hp > 0:
        y = zad(del1[st], hp, st, x, t)
        if y <= 0:
            map[mesto[0][x]][mesto[1][x]] = -100
            return 1

        return 0
    if hp <= 0:
        map[mesto[0][x]][mesto[1][x]] = -100
        return 1
def zad (del1, hp, st, x, t):
    global mesto, map
    mas=json.load(open(puti + str(x) + 'at.txt', 'r'))
    d1 = mesto[0][x]
    d2 = mesto[1][x]
    if del1 == mas[0]:
        if d2 != 49:
            if map[d1][d2+1] == -100:
                hp += 10
                map[d1][d2+1] = 100
            if map[d1][d2+1] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1][d2+1] == 0:
                map[d1][d2] = 0
                d2 += 1
                map[d1][d2] = 100
        st += 1
    if del1 == mas[1]:
        if d2 != 49 and d1 != 49:
            map[d1][d2] = 0
            if map[d1+1][d2+1] == -100:
                hp += 10
                map[d1+1][d2+1] = 100
            if map[d1+1][d2+1] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1+1][d2+1] == 0:
                map[d1][d2] = 0
                d2 += 1
                d1 += 1
                map[d1][d2] = 100
        st += 1



    if del1 == mas[2]:
        if d1 != 49:
            map[d1][d2] = 0
            if map[d1+1][d2] == -100:
                hp += 10
                map[d1+1][d2] = 100
            if map[d1+1][d2] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1+1][d2] == 0:
                map[d1][d2] = 0
                d1 += 1
                map[d1][d2] = 100
        st += 1

    if del1 == mas[3]:
        if d1 != 49 and d2 != 0:
            map[d1][d2] = 0
            if map[d1+1][d2-1] == -100:
                hp += 10
                map[d1+1][d2-1] = 100
            if map[d1+1][d2-1] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1+1][d2-1] == 0:
                map[d1][d2] = 0
                d1 += 1
                d2 -= 1
                map[d1][d2] = 100
        st += 1

    if del1 == mas[4]:
        if d2 != 0:
            map[d1][d2] = 0
            if map[d1][d2-1] == -100:
                hp += 10
                map[d1][d2-1] = 100
            if map[d1][d2-1] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1][d2-1] == 0:
                map[d1][d2] = 0
                d2 -= 1
                map[d1][d2] = 100
        st += 1

    if del1 == mas[5]:
        if d1 != 0 and d2 != 0:
            map[d1][d2] = 0
            if map[d1-1][d2-1] == -100:
                hp += 10
                map[d1-1][d2-1] = 100
            if map[d1-1][d2-1] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1-1][d2-1] == 0:
                map[d1][d2] = 0
                d1 -= 1
                d2 -= 1
                map[d1][d2] = 100
        st += 1

    if del1 == mas[6]:
        if d1 != 0:
            map[d1-1][d2] = 0
            if map[d1-1][d2] == -100:
                hp += 10
                map[d1-1][d2] = 100
            if map[d1-1][d2] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1-1][d2] == 0:
                map[d1][d2] = 0
                d1 -= 1
                map[d1][d2] = 100
        st += 1

    if del1 == mas[7]:
        if d2 != 49 and d1 != 0:
            map[d1-1][d2+1] = 0
            if map[d1-1][d2+1] == -100:
                hp += 10
                map[d1-1][d2+1] = 100
            if map[d1-1][d2+1] == -200:
                hp = -1
                map[d1][d2] = -100
            if map[d1-1][d2+1] == 0:
                map[d1][d2] = 0
                d1 -= 1
                d2 += 1
                map[d1][d2] = 100
        st += 1



    if del1 == 8:
        st += 1
        for u in range(len(mas)-1):
            mas[u] += 1
        mas[7] = 0
        t = (t+1) % 8


    if del1 == 9:
        st += 1
        for u in range(len(mas) - 2):
            mas[u] += 1
        mas[6] = 0
        mas[7] = 1
        t = (t+2) % 8

    if del1 == 10:
        st += 1
        for u in range(len(mas) - 3):
            mas[u] += 1
        mas[5] = 0
        mas[6] = 1
        mas[7] = 2
        t = (t+3) % 8

    if del1 == 11:
        st += 1
        for u in range(len(mas) - 4):
            mas[u] += 1
        mas[4] = 0
        mas[5] = 1
        mas[6] = 2
        mas[7] = 3
        t = (t+4) % 8

    if del1 == 12:
        st += 1
        for u in range(len(mas) - 4):
            mas[u] += 1
        mas[3] = 0
        mas[4] = 1
        mas[5] = 2
        mas[6] = 3
        mas[7] = 4
        t = (t+5) % 8

    if del1 == 13:
        st += 1
        for u in range(len(mas) - 4):
            mas[u] += 1
        mas[2] = 0
        mas[3] = 1
        mas[4] = 2
        mas[5] = 3
        mas[6] = 4
        mas[7] = 5
        t = (t+6) % 8

    if del1 == 14:
        st += 1
        for u in range(len(mas) - 4):
            mas[u] += 1
        mas[1] = 0
        mas[2] = 1
        mas[3] = 2
        mas[4] = 3
        mas[5] = 4
        mas[6] = 5
        mas[7] = 6
        t = (t+7) % 8




    if del1 == 15:
        if t == 0:
            if mesto[1][x] != 49:
                if map[d1][d2+1] == -100:
                    st += 1
                if map[d1][d2+1] == 0:
                    st += 2
                if map[d1][d2+1] > 0:
                    st += 3
                if map[d1][d2+1] == -200:
                    st += 4
        if t == 1:
            if d2 != 49 and d1 != 49:
                if map[d1+1][d2+1] == -100:
                    st += 1
                if map[d1+1][d2+1] == 0:
                    st += 2
                if map[d1+1][d2+1] > 0:
                    st += 3
                if map[d1+1][d2+1] == -200:
                    st += 4
        if t == 2:
            if d1 != 49:
                if map[d1+1][d2] == -100:
                    st += 1
                if map[d1+1][d2] == 0:
                    st += 2
                if map[d1[x]+1][d2] > 0:
                    st += 3
                if map[d1+1][d2] == -200:
                    st += 4
        if t == 3:
            if d1 != 49 and d2 != 0:
                if map[d1+1][d2-1] == -100:
                    st += 1
                if map[d1+1][d2-1] == 0:
                    st += 2
                if map[d1+1][d2-1] > 0:
                    st += 3
                if map[d1+1][d2-1] == -200:
                    st += 4
        if t == 4:
            if d2 != 0:
                if map[d1][d2-1] == -100:
                    st += 1
                if map[d1][d2-1] == 0:
                    st += 2
                if map[d1][d2-1] > 0:
                    st += 3
                if map[d1][d2-1] == -200:
                    st += 4
        if t == 5:
            if d1 != 0 and d2 != 0:
                if map[d1-1][d2-1] == -100:
                    st += 1
                if map[d1-1][d2-1] == 0:
                    st += 2
                if map[d1-1][d2-1] > 0:
                    st += 3
                if map[d1-1][d2-1] == -200:
                    st += 4
        if t == 6:
            if d1 != 0:
                if map[d1-1][d2] == -100:
                    st += 1
                if map[d1-1][d2] == 0:
                    st += 2
                if map[d1-1][d2] > 0:
                    st += 3
                if map[d1-1][d2] == -200:
                    st += 4
        if t == 7:
            if d2!=49 and d1 != 0:
                if map[d1-1][d2+1] == -100:
                    st += 1
                if map[d1-1][d2+1] == 0:
                    st += 2
                if map[d1-1][d2+1] > 0:
                    st += 3
                if map[d1-1][d2+1] == -200:
                    st += 4



    if del1 == 16:
        st += 1
        if t == 0:
            if d2 != 49:
                if map[d1][d2 + 1] == -100:
                    map[d1][d2 + 1] = -200
                if map[d1][d2 + 1] == -200:
                    map[d1][d2 + 1] = 0
                    hp+=10
        if t == 1:
            if d2 != 49 and d1 != 49:
                if map[d1 + 1][d2 + 1] == -100:
                    map[d1 + 1][d2 + 1] = -200
                if map[d1 + 1][d2 + 1] == -200:
                    map[d1 + 1][d2 + 1] = 0
                    hp += 10
        if t == 2:
            if d1 != 49:
                if map[d1 + 1][d2] == -100:
                    map[d1 + 1][d2] = -200
                if map[d1 + 1][d2] == -200:
                    map[d1 + 1][d2] = 0
                    hp += 10
        if t == 3:
            if d1 != 49 and d2 != 0:
                if map[d1 + 1][d2 - 1] == -100:
                    map[d1 + 1][d2 - 1] = -200
                if map[d1 + 1][d2 - 1] == -200:
                    map[d1 + 1][d2 - 1] = 0
                    hp += 10
        if t == 4:
            if d2 != 0:
                if map[d1][d2 - 1] == -100:
                    map[d1][d2 - 1] = -200
                if map[d1][d2 - 1] == -200:
                    map[d1][d2 - 1] = 0
                    hp += 10
        if t == 5:
            if d1 != 0 and d2 != 0:
                if map[d1 - 1][d2 - 1] == -100:
                    map[d1 - 1][d2 - 1] = -200
                if map[d1 - 1][d2 - 1] == -200:
                    map[d1 - 1][d2 - 1] = 0
                    hp += 10
        if t == 6:
            if d1 != 0:
                if map[d1 - 1][d2] == -100:
                    map[d1 - 1][d2] = -200
                if map[d1 - 1][d2] == -200:
                    map[d1 - 1][d2] = 0
                    hp += 10
        if t == 7:
            if d2 != 49 and d1 != 0:
                if map[d1 - 1][d2 + 1] == -100:
                    map[d1 - 1][d2 + 1] = -200
                if map[d1 - 1][d2 + 1] == -200:
                    map[d1 - 1][d2 + 1] = 0
                    hp += 10
    if del1 == 16:
        st += 2
    if del1 == 17:
        st += 3
    if del1 == 18:
        st += 4
    if del1 == 19:
        st += 5
    if del1 == 20:
        st += 6
    if del1 == 21:
        st += 7
    if del1 == 22:
        st += 8
    if del1 == 23:
        st += 9
    if del1 == 24:
        st += 10
    if del1 == 25:
        st += 11
    if del1 == 26:
        st += 12
    if del1 == 27:
        st += 13
    if del1 == 28:
        st += 14
    if del1 == 29:
        st += 15
    if del1 == 30:
        st += 16
    if del1 == 31:
        st += 17
    if del1 == 32:
        st += 18
    if del1 == 33:
        st += 19
    if del1 == 34:
        st += 20
    if del1 == 35:
        st += 21
    if del1 == 36:
        st += 22
    if del1 == 37:
        st += 23
    if del1 == 38:
        st += 24
    if del1 == 39:
        st += 25
    if del1 == 40:
        st += 26
    if del1 == 41:
        st += 27
    if del1 == 42:
        st += 28
    if del1 == 43:
        st += 29
    if del1 == 44:
        st += 30
    hp-=1
    mesto[0][x] = d1
    mesto[1][x] = d2
    json.dump(st, open(puti + str(x) + 'str.txt', 'w', encoding="UTF-8"))
    json.dump(map, open(put + 'map.txt', 'w', encoding="UTF-8"))
    json.dump(mesto, open(put + 'mesto.txt', 'w', encoding="UTF-8"))
    json.dump(mas, open(puti + str(x) + 'at.txt', 'w', encoding="UTF-8"))
    json.dump(hp, open(puti + str(x) + 'hp.txt', 'w', encoding="UTF-8"))
    return hp