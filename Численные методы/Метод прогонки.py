def is_no_correct(n, m, system):
    for i in range(n):
        for j in range(m):
            if j - i > 1:
                if system[i][j] != 0:
                    return False
            if i - j > 1:
                if system[i][j] != 0:
                    return False
    return True


def fill_matrix_from_file(system, system_answer, n, m):
    input = open('Test2.txt', 'r')
    s = input.readlines()

    for i, line in enumerate(s):
        if i == 0:
            n = line
            n = int(n)
            m = n
        else:
            rows = line.strip().split(' ')
            row = []
            row = rows[:-1]
            for i in range(n):
                row[i] = int(row[i])
            system.append(row)

            last_elem = int(rows[-1])
            system_answer.append(last_elem)
    return system, system_answer, n, m

def system_solution(massA, massB, massX, system, system_answer):
    massA[0] = - (system[0][1] / system[0][0])
    massB[0] = system_answer[0] / system[0][0]
    # print('i =', 0,'    ', massA[0], massB[0])
    massA[1] = 1
    massB[1] = 0
    # print('i =',1, '    ', massA[0], massB[0])
    for i in range(1, n - 1):
        # print('i =', i+1, end ='     ')
        massA[i + 1] = (-massA[i - 1] * system[i][i - 1] - massA[i] * system[i][i]) / system[i][i + 1]
        massB[i + 1] = (system_answer[i] - system[i][i - 1] * massB[i - 1] - system[i][i] * massB[i]) / system[i][i + 1]
        # print(massA[i+1], massB[i+1])
    if (system[n - 1][n - 2] * massA[n - 2] + system[n - 1][n - 1] * massA[n - 1]) == 0:
        print('Определитель матрицы равен 0')
    else:
        t = (system_answer[n - 1] - system[n - 1][n - 2] * massB[n - 2] - system[n - 1][n - 1] * massB[n - 1]) / (
                    system[n - 1][n - 2] * massA[n - 2] + system[n - 1][n - 1] * massA[n - 1])
        massX[n - 1] = round(massA[n - 1] * t + massB[n - 1])
        # print(massX[n-1])
        for i in range(n - 1, -1, -1):
            # print(i)
            massX[i] = round(massA[i] * t + massB[i])
        print('Решение системы:', massX)

system = []
system_answer = []
n = 0
m = 0
system, system_answer, n, m = fill_matrix_from_file(system, system_answer, n, m)

massX = [0]*n
massA = [0]*n
massB = [0]*n

if not is_no_correct(n, m, system):
    print('Матрица не трехдиагональная')
else:
    system_solution(massA, massB, massX, system, system_answer)
