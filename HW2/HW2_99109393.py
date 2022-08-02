from math import *
import decimal

expression = input()
x0, x1 = input().split()
x0, x1 = [decimal.Decimal(x0), decimal.Decimal(x1)]

decimal.getcontext().prec = int(-log10(float(input())))

print(expression, x0, x1)

def value(expression, c):
    x = decimal.Decimal(c)
    return decimal.Decimal(eval(expression))

temp = decimal.Decimal(0)
x3 = decimal.Decimal(1)

while (temp != x3):
    f0 = decimal.Decimal(value(expression, x0))
    f1 = decimal.Decimal(value(expression, x1))
    
    temp, x3 = x3, (x0 * f1 - x1 * f0) / (f1 - f0)
    f3 = decimal.Decimal(value(expression, x3))

    print(x3)

    if f3 > 0:
        if f0 <= 0:
            x0, x1 = x0, x3
        elif f1 <= 0:
            x0, x1 = x1, x3
        else:
            raise Exception("Can't find root in the given interval")
    else:
        if f0 >= 0:
            x0, x1 = x3, x0
        elif f1 >= 0:
            x0, x1 = x3, x1
        else:
            raise Exception("Can't find in the given interval")
