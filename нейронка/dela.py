def f(mas, ma, p):
    p += 1
    y = len(ma[0])
    for j in range(y):
        if mas[ma[[0]] - 1][ma[[1]]] != -1:
            ma[0].append(ma[0] - 1)
            ma[1].append(ma[0])

        if mas[ma[0] - 1][ma[0] + 1] != -1:
            ma[0].append(ma[0] - 1)
            ma[1].append(ma[0] + 1)

        if mas[ma[0]][ma[0] + 1] != -1:
            ma[0].append(ma[0])
            ma[1].append(ma[0] + 1)

        if mas[ma[0] + 1][ma[0] + 1] != -1:
            ma[0].append(ma[0] + 1)
            ma[1].append(ma[0] + 1)

        if mas[ma[0] + 1][ma[0]] != -1:
            ma[0].append(ma[0] + 1)
            ma[1].append(ma[0])

        if mas[ma[0] - 1][ma[0] - 1] != -1:
            ma[0].append(ma[0] - 1)
            ma[1].append(ma[0] - 1)

        if mas[ma[0]][ma[0] - 1] != -1:
            ma[0].append(ma[0])
            ma[1].append(ma[0] - 1)

        if mas[ma[0] + 1][ma[0] - 1] != -1:
            ma[0].append(ma[0] + 1)
            ma[1].append(ma[0] - 1)

    for j in range(len(ma[0])):
        ma
    print(ma)
    p = f(mas, ma, p)
    return p

mas = []
e = input()
y = 0
q = ''
w = ''
for j in e:
    if j == " ":
        y = 1
    if j != " " and y == 0:
        q += j
    if j != " " and y == 1:
        w += j
q = int(q)
w = int(w)
l = 0
for j in range(q):
    t = input()
    mas.append([])
    for u in t:
        if u == "#":
            mas[j].append(-1)
        if u == ".":
            mas[j].append(0)
        if u == "T":
            mas[j].append(1)
ma = [[1], [1]]
print(ma)
p = 0
p = f(mas, ma, p)
