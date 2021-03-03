import numpy as np
import ap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
import pasha
import json
import taracan
import zero
import eat
plt.ion()
fig = plt.figure()
#ax = fig.add_sublot(111)
puti = "D:\\нейронка\\"
t=0
p=0
die = []
while p<2000:
    for j in range(49):
        #map = json.load(open(puti + 'map.txt', 'r'))
        print (len(die))
        t = taracan.robot(j)
        if t==1 and not(j in die):
            die.append(j)
        if len(die) == 42:
            break


    if len(die) == 42:
        print(p)
        p = 0
        die = []
        zero.zero()
        ap.zero()
    # Eat
    eat.gen()
    # // Vizualization //
    mop = np.array(json.load(open(puti + 'map.txt', 'r')))
    plt.clf()
    plt.imshow(mop)
    fig.canvas.draw()
    plt.pause(0.001)
    plt.show()

    t=0
    p+=1