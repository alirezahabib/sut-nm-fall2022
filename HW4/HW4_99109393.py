import math
import matplotlib.pyplot as plt


def f(s):
    return lambda x: x ** s * math.exp(x)


def simpson3(f, a, b, n):
    n -= n % 2 - 1  # oddization (!)

    tot = 0
    h = (b - a) / n

    for i in range(0, n + 1):
        if i == 0 or i == n:
            c = 1
        elif i % 2:
            c = 4
        else:
            c = 2

        x = a + h * i
        tot += c * f(x)

    return tot * h / 3


def simpson38(f, a, b, n):
    n -= n % 3 - 3  # make n divisible by 3

    tot = 0
    h = (b - a) / n

    for i in range(0, n + 1):
        if i == 0 or i == n:
            c = 1
        elif i % 3:
            c = 3
        else:
            c = 2

        x = a + h * i
        tot += c * f(x)

    return tot * h * 3 / 8


def trapezoidal(f, a, b, n):
    tot = 0
    h = (b - a) / n

    for i in range(0, n + 1):
        if i == 0 or i == n:
            c = 1
        else:
            c = 2

        x = a + h * i
        tot += c * f(x)

    return tot * h / 2


if __name__ == '__main__':
    n = 10
    a = 1
    b = 2
    s = 2

    print(f'f(s = {s}, x = {a}) = {f(s)(a)}')
    print(f'f(s = {s}, x = {b}) = {f(s)(b)}', '\n')

    h_data = []
    simpson3_data = []
    simpson38_data = []
    trapezoidal_data = []

    for i in range(n):
        h_data.append(1 / 2 ** i)
        simpson3_data.append(simpson3(f(s), a, b, 2 ** i))
        simpson38_data.append(simpson38(f(s), a, b, 2 ** i))
        trapezoidal_data.append(trapezoidal(f(s), a, b, 2 ** i))

        print('h = ', h_data[-1])
        print('Simpson 1/3 estimation:', simpson3_data[-1])
        print('Simpson 3/8 estimation:', simpson38_data[-1])
        print('Trapezoidal estimation:', trapezoidal_data[-1], '\n')

    plt.plot(h_data, simpson3_data, '-bo', label='Simpson 1/3')
    plt.plot(h_data, simpson38_data, '-go', label='Simpson 3/8')
    plt.plot(h_data, trapezoidal_data, '-ro', label='Trapezoidal')
    plt.legend()
    plt.title(r'$\int_1^2{x^s e^x dx}$ for $s = 2$')
    plt.xlabel('h')

    plt.savefig('plot.png', dpi=600)
    plt.savefig('plot.pdf')
    plt.show()


'''
!!! I have appended the plots to the end of the theory part's file !!!

The Trapezoidal method is a little off at first, but apparently, it converges faster than Simpson 1/3.
Simpson 3/8 is the best, converging fast and low error even with a high "h".

(Note that n is rounded up to the nearest multiple of 3 for Simpson 3/8
so h = 1 is changed to h = 1/3 on this method, but still, it is the best)

console output:

/Users/alireza/.pyenv/versions/3.10.3/bin/python /Users/alireza/SUT/NA/HW4_99109393.py
f(s = 2, x = 1) = 2.718281828459045
f(s = 2, x = 2) = 29.5562243957226

h =  1.0
Simpson 1/3 estimation: 10.758168741393883
Simpson 3/8 estimation: 12.078519010384435
Trapezoidal estimation: 16.137253112090825

h =  0.5
Simpson 1/3 estimation: 9.851725972850119
Simpson 3/8 estimation: 12.078519010384435
Trapezoidal estimation: 13.110526760175734

h =  0.25
Simpson 1/3 estimation: 10.481035410958478
Simpson 3/8 estimation: 12.061042221843653
Trapezoidal estimation: 12.324546271663287

h =  0.125
Simpson 1/3 estimation: 11.086550099699709
Simpson 3/8 estimation: 12.060071408918049
Trapezoidal estimation: 12.126138306912619

h =  0.0625
Simpson 1/3 estimation: 11.514368224090775
Simpson 3/8 estimation: 12.059845497238571
Trapezoidal estimation: 12.076415435193235

h =  0.03125
Simpson 1/3 estimation: 11.770328241273132
Simpson 3/8 estimation: 12.059831709804879
Trapezoidal estimation: 12.063977141271854

h =  0.015625
Simpson 1/3 estimation: 11.910591753026308
Simpson 3/8 estimation: 12.059830453203428
Trapezoidal estimation: 12.060867093963736

h =  0.0078125
Simpson 1/3 estimation: 11.984049727168092
Simpson 3/8 estimation: 12.059830375144738
Trapezoidal estimation: 12.060089552517338

h =  0.00390625
Simpson 1/3 estimation: 12.021644610769771
Simpson 3/8 estimation: 12.059830369761167
Trapezoidal estimation: 12.059895165304441

h =  0.001953125
Simpson 1/3 estimation: 12.040662981515517
Simpson 3/8 estimation: 12.059830369425212
Trapezoidal estimation: 12.059846568385526


Process finished with exit code 0
'''
