import json
import random
puti = "D:\\нейронка\\"
def gen():
    map = json.load(open(puti + 'map.txt', 'r'))
    for i in range(49):
        x = random.randint(0,49)
        y = random.randint(0,49)
        if map[x][y] == 0:
            map[x][y] = -100
    json.dump(map, open(puti + 'map.txt', 'w', encoding="UTF-8"))
