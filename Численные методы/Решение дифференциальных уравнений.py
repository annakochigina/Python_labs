def fun(x,y):
    return x-y-1


def rung(n, x, y, h):
    for i in range(n):
        k1 = h * fun(x, y)
        k2 = h * fun(x + (h / 2), y + (k1 / 2))
        k3 = h * fun(x + (h / 2), y + (k2 / 2))
        k4 = h * fun(x + h, y + k3)
        dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y = y + dy
        x = x + h
    return y


print('Точное значение функции в точке 0.1 - 0.814512254')
print('Точное значение функции в точке 2 - 0.4060058496')
print()

a = 0
n = 10000
#метод Рунге-Кутта 1-ого порядка для точки 0.1
b = 0.1
h = (b - a) / n
x = 0
y = 1
i = 0
while x <= b:
    i += 1
    y = y + h * fun(x, y)
    x = a + (i * h)
print('Метод Рунге-Кутта 1-ого порядка в точке 0.1:', y)
#метод Рунге-Кутта 1-ого порядка для точки 2
b = 2
h = (b - a) / n
x = 0
y = 1
i = 0
while x != b:
    i += 1
    y = y + h * fun(x, y)
    x = a + (i * h)
print('Метод Рунге-Кутта 1-ого порядка в точке 2:', y)
print()

#метод Рунге-Кутта 2-ого порядка для точки 0.1
b = 0.1
h = (b - a) / n
x = 0
y = 1
z = 0
i = 0
while x != b:
    i += 1
    z = y + (h / 2) * fun(x, y)
    y = y + h * fun (x + (h / 2), z)
    x = a + (i * h)
print('Метод Рунге-Кутта 2-ого порядка в точке 0.1:', y)
#метод Рунге-Кутта 2-ого порядка для точки 2
b = 2
h = (b - a) / n
x = 0
y = 1
z = 0
i = 0
while x != b:
    i += 1
    z = y + (h / 2) * fun(x, y)
    y = y + h * fun (x + (h / 2), z)
    x = a + (i * h)
print('Метод Рунге-Кутта 2-ого порядка в точке 2:', y)
print()

#метод Рунге-Кутта 4-ого порядка для точки 0.1
b = 0.1
n = 10000
h = (b - a) / n
x = 0
y = 1
k1, k2, k3, k4 = 0, 0, 0, 0
dy = 0
for i in range(n):
    k1 = h * fun(x, y)
    k2 = h * fun(x + (h / 2), y + (k1 / 2))
    k3 = h * fun(x + (h / 2), y + (k2 / 2))
    k4 = h * fun(x + h, y + k3)
    dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    y = y + dy
    x = x + h
print('Метод Рунге-Кутта 4-ого порядка в точке 0.1:', y)
#метод Рунге-Кутта 4-ого порядка для точки 2
b = 2
n = 10000
h = (b - a) / n
x = 0
y = 1
k1, k2, k3, k4 = 0, 0, 0, 0
dy = 0
for i in range(n):
    k1 = h * fun(x, y)
    k2 = h * fun(x + (h / 2), y + (k1 / 2))
    k3 = h * fun(x + (h / 2), y + (k2 / 2))
    k4 = h * fun(x + h, y + k3)
    dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    y = y + dy
    x = x + h
print('Метод Рунге-Кутта 4-ого порядка в точке 2:', y)
print()

#метод двойного счёта
a = 0
b = 0.1
n = 1
h = (b - a) / n
x = 0
y = 1
eps = 10 ** (-10)
end1 = 0
end2 = rung(n, x, y, h)
while (abs(end1 - end2)) / 15 > eps:
    n = 2 * n
    h = (b - a) / n
    end1 = end2
    end2 = rung(n, x, y, h)
print('Метод двойного счёта в точке 0.1:', "{0:.10f}".format(end2))

a = 0
b = 2
n = 1
h = (b - a) / n
x = 0
y = 1
eps = 10 ** (-10)
end1 = 0
end2 = rung(n, x, y, h)
while (abs(end1 - end2)) / 15 > eps:
    n = 2 * n
    h = (b - a) / n
    end1 = end2
    end2 = rung(n, x, y, h)
print('Метод двойного счёта в точке 2:', "{0:.10f}".format(end2))