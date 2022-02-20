import math

def fun (x):
    return (math.exp(x) - x - 5)

a, b = map(float, input().split())
eps = 10 ** (-8)
count = 0
c = 0

while abs(b-a) > 2*eps:
    c = (a + b) / 2
    count += 1
    if (fun(a) * fun(c)) > 0:
        a = c
    else:
        b = c

print(c, count)