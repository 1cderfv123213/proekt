X1 = 0 #Переменная X наидальшего выстрела
Y1 = 0 #Переменная Y наидальшего выстрела
X0 =int(input()) #Принимаем X0 и преобразуем их в целочисленные, из строк которые принимает питон
Y0 =int(input()) #Принимаем Y0 и преобразуем их в целочисленные, из строк которые принимает питон
i = 0 #номр выстрела
T = 0 #Переменная наидальшего выстрела
N = int(input()) #Принимаем количество выстрелов и преобразуем их в целочисленные, из строк которые принимает питон
for j in range(N): #Цикол позволяющий принять все X и Y
    X = int(input())#Принимаем X и преобразуем их в целочисленные, из строк которые принимает питон
    Y = int(input())#Принимаем Y и преобразуем их в целочисленные, из строк которые принимает питон
    X = X - X0 #переводим наш полученный X в то положение в котором он бы находился при условии что X0 = 0
    Y = Y - Y0 #переводим наш полученный Y в то положение в котором он бы находился при условии что Y0 = 0
    Z = X*X + Y*Y #Сумирую квадраты заначений X и Y из-за формулы пифагора сумма квадратов 2 катитов равна квадрату гипотенузы а наибольший квадрат гипотенузы имеит наибольшая гипотенуза а гипотенуза это отрезок от мишени до места поподания
    if Z > T: #Сравниваем нашу наидольнейшую точку с нашим новым выстрелом
        T = Z #Приравниваем к нанаильнейший выстрил к новому выстрлу при условию если данный выстрел дальше
        X1 = X #Приравниваем К нашей переменной X наидальшего выстрела новый X при условию если данный выстрел дальше
        Y1 = Y #Приравниваем К нашей переменной Y наидальшего выстрела новый Y при условию если данный выстрел дальше
        i = j+1 #Приравниваем К нашему номеру наидальшего выстрела новый номер при условию если данный выстрел дальше
print("X самого дального выстрела = ", X1)#Вывод
print("Y самого дального выстрела = ", Y1)#Вывод
print("i самого дального выстрела = ", i)#Вывод