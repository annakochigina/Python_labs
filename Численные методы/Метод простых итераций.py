def q1(matr):
    sum_max = 0
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += abs(matr[i][j])
        if sum > sum_max:
            sum_max = sum
    return sum_max

def q2(matr):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += (matr[i][j]) ** 2
    return sum ** (1/2)

def qb(matr):
    sum_max = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += abs(matr[i][j])
        if sum > sum_max:
            sum_max = sum
    return sum_max

def fun_norma(norma, flag):
    eps = 0.000001
    if norma <= eps * ((1 - q)/q):
        flag = True
    return flag

def mass(matr,matr_otv, x0, x1):
    n = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += x0[j]*matr[i][j]
            print(sum)
        x1[i] = sum + matr_otv[i]
        print(x1[i])
    return x1

def normq1(matr, x0, x1):
    for i in range(n):
        x1[i] = 0

    summa = 0
    x1 = mass(matr, matr_otv, x0, x1)

    for i in range(n):
        summa += abs(x1[i] - x0[i])

    for i in range(n):
        x0[i] = x1[i]
    return summa, x0, x1

def normq2(matr, x0, x1):
    for i in range(n):
        x1[i] = 0
    summa = 0
    x1 = mass(matr, matr_otv, x0, x1)

    for i in range(n):
        summa += (x1[i] - x0[i]) ** 2

    for i in range(n):
        x0[i] = x1[i]
    return summa ** 0.5, x0, x1

def normqb(matr, x0, x1):
    for i in range(n):
        x1[i] = 0
    summa = 0
    x1 = mass(matr, matr_otv, x0, x1)

    max = 0
    for i in range(n):
        if abs(x1[i] - x0[i]) > max:
            max = abs(x1[i] - x0[i])

    for i in range(n):
        x0[i] = x1[i]
    return max, x0, x1

matr1 = [[8, 11, 25], [7, -50, -12], [10, 1, -3]]
matr_otv1 = [-48, 0, 30]
matr = [[0, -0.1, 0.3], [7/50, 0, 12/50], [-8/25, -11/25, 0]]
matr_otv = [3, 0, -48/25]
n = 3
mass_q = [0]*n
mass_q[0] = q1(matr)
mass_q[1] = q2(matr)
mass_q[2] = qb(matr)

for i in range(n):
    if mass_q[i] >= 1:
        mass_q[i] = 2
q = min(mass_q)

if q > 1:
    print('Метод простых итераций не применим')
    exit()
print('Метод простых итераций применим')

ind = mass_q.index(min(mass_q))
x0 = [0, 0, 0]
x1 = [0, 0, 0]
flag = False
norma = 0
if ind == 0:
    while flag == False:
        norma, x0, x1 = normq1(matr, x0, x1)
        flag = fun_norma(norma, flag)
    print(x0)
elif ind == 1:
    while flag == False:
        norma, x0, x1 = normq2(matr, x0, x1)
        flag = fun_norma(norma, flag)
    print(x0)
else:
    while flag == False:
        norma, x0, x1 = normqb(matr, x0, x1)
        flag = fun_norma(norma, flag)
    print(x0)


