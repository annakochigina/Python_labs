def start(mass):
    i = 0
    for i in range(3):
        for j in range(6):
            if j == 0:
                mass[i][j] = system_answer[i]
            else:
                mass[i][j] = system[i][j - 1]
    i = 3
    k = 0
    mass[3][0] = 0
    for j in range(1, 6):
        mass[i][j] = function[k]
        k += 1
    return mass

def resolving_element(mass, jmax, imin, per_element, basic):
    last_row = mass[-1][1:-1]
    maximum = max(last_row)
    jmax = last_row.index(maximum) + 1

    j = 6
    for i in range(3):
        mass[i][j] = mass[i][0] / mass[i][jmax]

    j = 6
    min = mass[0][6]
    imin = 0
    for i in range(3):
        if (mass[i][j] > 0) and (mass[i][j] < min):
            min = mass[i][j]
            imin = i

    per_element = mass[imin][jmax]

    basic[imin] = jmax
    return mass, jmax, imin, per_element, basic

def double(mass, mass_double):
    for i in range(4):  # создаем дубль таблицы
        for j in range(7):
            mass_double[i][j] = mass[i][j]
            mass[i][j] = -1
    return mass, mass_double

def basicX(mass):
    i = -1  # заполняем столбцы с базисным х
    for elem in basic:
        i += 1
        for j in range(6):
            if j == elem:
                for k in range(4):
                    if k == i:
                        mass[k][j] = 1
                    else:
                        mass[k][j] = 0
    return mass

def table(mass):
    for i in range(4):  # заполняем таблицу
        for j in range(6):
            if mass[i][j] == -1:
                if i == imin:
                    mass[i][j] = mass_double[i][j] / per_element
                else:
                    mass[i][j] = mass_double[i][j] - ((mass_double[i][jmax] * mass_double[imin][j]) / per_element)
    return mass

def is_row_no_positive(mass):
    last_row = mass[-1]
    for i in last_row[1:-1]:
        if i > 0:
            return True
    return False

system = [[1, 9, 1, 0, 0], [3, 2, 0, 1, 0], [5, 1, 0, 0, 1]]
system_answer = [810, 430, 600]
function = [1, 1, 0, 0, 0]
basic = [3, 4, 5]
mass = [[-1]*7, [-1]*7, [-1]*7, [-1]*7]
mass_double = [[-1]*7, [-1]*7, [-1]*7, [-1]*7]

mass = start(mass)

while is_row_no_positive(mass):
    jmax, imin, per_element = 0, 0, 0
    mass, jmax, imin, per_element, basic = resolving_element(mass, jmax, imin, per_element, basic)
    mass, mass_double = double(mass, mass_double)
    mass = basicX(mass)
    mass = table(mass)

for i in range(4):
    for j in range(7):
        print(mass[i][j], end = '  ')
    print()
print()

for i, elm in enumerate(basic):
    basic[i] = elm-1

result_basic = [0, 0, 0, 0, 0]
j = 0
for i, elem in enumerate(basic):
    result_basic[elem] = mass[i][0]

print('Базисное решение:', result_basic)
print('Функция: f =', mass[3][0] * (-1))
