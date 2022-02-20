import math
import numpy

def fun(x, y, sumx2i, sumxyi, sumxi, sumyi):
    x2i = x ** 2
    xyi = x * y
    sumx2i += x2i
    sumxyi += xyi
    sumxi += x
    sumyi += y
    return sumx2i, sumxyi, sumxi, sumyi


def glob(sumx2, sumxy, sumx, sumy):
    Mxx = sumx2 / n
    Mxy = sumxy / n
    Mx = sumx / n
    My = sumy / n

    M1 = numpy.array([[Mxx, Mx], [Mx, 1]])
    V1 = numpy.array([Mxy, My])
    ak = numpy.linalg.solve(M1, V1)[0]
    a.append(ak)
    bk = numpy.linalg.solve(M1, V1)[1]
    b.append(bk)
    return ak, bk


def linfun(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(X[i], Y[i], sumx2, sumxy, sumx, sumy)
    ad, bd = glob(sumx2, sumxy, sumx, sumy)
    sump = 0
    for i in range(n):
        sump = sump + ((ad * X[i] + bd) - Y[i]) ** 2
    r.append(sump)
    return ad, bd, sump

def hyperbole(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(X[i], 1/Y[i], sumx2, sumxy, sumx, sumy)
    ad, bd = glob(sumx2, sumxy, sumx, sumy)
    sump = 0
    for i in range(n):
        sump = sump + ((1 / (ad*X[i] + bd)) - Y[i]) ** 2
    r.append(sump)
    return ad, bd, sump

def logarithm(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(math.log(X[i]), Y[i], sumx2, sumxy, sumx, sumy)
    ad, bd = glob(sumx2, sumxy, sumx, sumy)
    sump = 0
    for i in range(n):
        sump = sump + ((ad * math.log(X[i]) + bd) - Y[i]) ** 2
    r.append(sump)
    return ad, bd, sump

def six(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(1/X[i], Y[i], sumx2, sumxy, sumx, sumy)
    ad, bd = glob(sumx2, sumxy, sumx, sumy)
    sump = 0
    for i in range(n):
        sump = sump + (((ad / X[i]) + bd) - Y[i]) ** 2
    r.append(sump)
    return ad, bd, sump

def seven(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(1/X[i], 1/Y[i], sumx2, sumxy, sumx, sumy)
    ad, bd = glob(sumx2, sumxy, sumx, sumy)
    sump = 0
    for i in range(n):
        sump = sump + ((X[i] / (ad * X[i] + bd)) - Y[i]) ** 2
    r.append(sump)
    return ad, bd, sump

def degree(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    ad = 0
    bd = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(math.log(X[i]), math.log(Y[i]), sumx2, sumxy, sumx, sumy)
    glob(sumx2, sumxy, sumx, sumy)

    ad = math.exp(b[len(b) - 1])
    bd = a[len(a) - 1]
    a[len(a) - 1] = ad
    b[len(b) - 1] = bd
    sump = 0
    for i in range(n):
        nm = X[i] ** bd
        sump = sump + ((ad * (X[i] ** bd)) - Y[i]) ** 2
    r.append(sump)


def exh(n):
    sumx2 = 0
    sumxy = 0
    sumx = 0
    sumy = 0
    ad = 0
    bd = 0
    for i in range(n):
        sumx2, sumxy, sumx, sumy = fun(X[i], math.log(Y[i]), sumx2, sumxy, sumx, sumy)
    glob(sumx2, sumxy, sumx, sumy)
    ad = math.exp(b[len(b) - 1])
    bd = a[len(a) - 1]
    a[len(a) - 1] = ad
    b[len(b) - 1] = bd
    sump = 0
    for i in range(n):
        sump = sump + ((ad * math.exp(bd*X[i])) - Y[i]) ** 2
    r.append(sump)


name_fun = ['линейная - y = a * x + b', 'степенная - y = a * x^n', 'показательная - y = a * e^(nx)', 'гиперболическая - y = 1 / (a * x + b)', 'логарифмическая y = a * ln(x) + b', 'y = a / x + b', 'y = x / (a * x + b)']
X = [0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2]
Y = [27.02, 20.02, 14.83, 10.98, 8.14, 6.03, 4.47]
a = []
b = []
r = []
n = len(X)

linfun(n)
degree(n)
exh(n)
hyperbole(n)
logarithm(n)
six(n)
seven(n)

ind = r.index(min(r))
print('Функция', name_fun[ind])
print('Точность приближения', min(r))
