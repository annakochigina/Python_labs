import math

a, b = map(float, input().split())
q = float (input())
eps = 10 ** (-8)
count = 0
c = 0

a = math.log(a+5, math.exp(1))
b = math.log(a+5, math.exp(1))

while abs(b-a) >= ((1-q)/q)*eps:
    count += 1
    a = b
    b = math.log(a + 5, math.exp(1))

print(b, count)
