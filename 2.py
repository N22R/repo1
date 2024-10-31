import math

a = 3
b = 4
h = 0.1
d = 0.001
x = a


def a(x):
    k = 1
    while x <= b:
        task = ((-1) ** k * math.sin(k ** x) / k)
        if abs(task) < d:
            break
        k += 1
        return task


while x <= b:
    print((x), '\t\t', (a(x)))
    x += h
    x = round(x, 3)
