import math

def Fun (x):
    return (math.exp(x)-x-5)

def Funpr (x):
    return(math.exp(x)-1)

def Funpr2(x):
    return math.exp(x)

a, b = map(float, input().split())
eps = 10 ** (-8)
count = 0
c = 0

if (Fun(b) * Funpr2(b)) < 0:
    a, b = b, a

while abs(b-a) > 2*eps:
    count += 1
    a = a - Fun(a)*((b-a)/(Fun(b)-Fun(a)))
    b = b - (Fun(b)/Funpr(b))

print((a+b)/2, count)