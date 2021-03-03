import json
import random
def zero():
    puti = "D:\\нейронка\\pamiati\\"
    t = 100
    k = 0
    p = 0
    mas = []
    for j in range(49):
        j = str(j)
        hp = json.load(open(puti + j + 'hp.txt', 'r'))
        json.dump(0, open(puti + j + 'str.txt', 'w', encoding="UTF-8"))
        if hp > 0:
            mas.append(j)
            json.dump(100, open(puti + j + 'hp.txt', 'w', encoding="UTF-8"))
    mos = json.load(open(puti + str(mas[len(mas)-1]) + '.txt', 'r'))
    x = random.randint(1, 5)
    for j in range(x):
        r = random.randint(0, 58)
        mos[r]=random.randint(0, 44)
    for j in range(49):
        j = str(j)
        hp = json.load(open(puti + j + 'hp.txt', 'r'))
        if hp <= 0:
            json.dump(100, open(puti + j + 'hp.txt', 'w', encoding="UTF-8"))
            cikl = json.load(open(puti + mas[k] + '.txt', 'r'))
            #print(k)
            json.dump(cikl, open(puti + j + '.txt', 'w', encoding="UTF-8"))
            if p == 6:
                k+=1
                p=0
            p+=1