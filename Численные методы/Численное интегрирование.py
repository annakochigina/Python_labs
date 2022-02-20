import math


def fun(x): #функция для вычисления функции ln от x
    return math.log(13 / (5 * x + 3))


def simp(x): #функция для вычисления метода симсона
    i = 0
    res = 0
    h = (b-a) / n
    for i in range(n):
        res = res + ((h / 6) * fun(a + i * h)) + (((2 * h) / 3) * fun(a + (i + 0.5) * h)) + ((h / 6) * fun(a + (i + 1) * h))
    return res


a = 1
b = 6
n = 100
h = (b - a) / n
z = 5*math.log(13)-(33/5)*math.log(33)+(8/5)*math.log(8)+5
print('Точное значение интеграла:', z)
print()

#метод треугольников
summa = 0
result = 0
i = 0
for i in range(n):
    summa = summa + fun(a + (i + 0.5) * h)
result = h*summa
print('Метод прямоугольников:', result)
print('Погрешность метода прямоугольников:', abs(z - result))
print()

#метод трапеций
summa = 0
result = 0
i = 0
for i in range(n):
    summa = summa + fun(a + (i * h))
result = (h/2) * (fun(a) + fun(b)) + (h * summa)
print('Метод трапеций:', result)
print('Погрешность метода трапеций:', abs(z - result))
print()

#метод Симпсона
summa = 0
result = 0
i = 0
for i in range(n):
    summa = summa + ((h / 6) * fun(a + i * h)) + (((2 * h) / 3) * fun(a + (i + 0.5) * h)) + ((h / 6) * fun(a + (i + 1) * h))
print('Метод Симпсона:', summa)
print('Погрешность метода Симпсона:', abs(z - summa))

#метод двойного счёта
eps = 10 ** (-8)
end1 = 0
end2 = h * fun(a)
while (abs(end1 - end2)) / 15 > eps:
    end1 = end2
    end2 = simp(n)
    n = 2 * n
print('Метод двойного счёта:', "{0:.8f}".format(end2))