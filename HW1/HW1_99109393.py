from decimal import *


def calc_e(x, n):
    A = [0.0] * n
    t = 1

    for i in range(n):
        A[i] = Decimal(t)
        t *= Decimal(Decimal(x) / (i + 1))

    e1 = 0
    e2 = 0

    for i in range(n):
        e1 += A[i]
        e2 += A[n-i-1]

    print(f'\nnumber of terms = {n}')
    print(f'(normal sum)  e^{x} = {e1}')
    print(f'(reverse sum) e^{x} = {e2}')


def test_precision(precision, x):
    getcontext().prec = precision
    print(f'\n\n{precision} digit precision')

    calc_e(x, 5)
    calc_e(x, 10)
    calc_e(x, 20)
    calc_e(x, 50)
    calc_e(x, 100)
    calc_e(x, 1000)
    calc_e(x, 10000)
    calc_e(x, 100000)


def main():
    x = -30

    test_precision(15, x)
    test_precision(20, x)
    test_precision(25, x)
    test_precision(30, x)
    test_precision(35, x)
    test_precision(40, x)


if __name__ == "__main__":
    main()
    