import json
import random
import ap
puti = "D:\\нейронка\\pamiati\\"
d = [0,1,2,3,4,5,6,7]
# for i in range(49):
#
#
ap.zero()
for i in range(49):
     json.dump(0, open(puti + str(i) + 'str.txt', 'w', encoding="UTF-8"))
     json.dump(100, open(puti + str(i) + 'hp.txt', 'w', encoding="UTF-8"))
     a = []
     for j in range(59):
          r = random.randint(0, 44)
          a.append(r)
     json.dump(a, open(puti + str(i) + '.txt', 'w', encoding="UTF-8"))
     json.dump(d, open(puti + str(i) + 'at.txt', 'w', encoding="UTF-8"))