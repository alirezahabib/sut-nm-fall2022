# q_7_1
import matplotlib.pyplot as plt
import numpy as np

# q_7_2
from sympy import Function, dsolve, Derivative
from sympy.abc import x


# runge kutta midpoint method for solving differential equations
def runge_kutta(f, x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    return y + k2


def q_7_1():
    h = 0.4
    end = 10
    f = lambda x, y: x + y

    x = np.arange(0, end + h, h)
    y = np.zeros(len(x))
    y[0] = 1

    for i in range(1, len(x)):
        y[i] = runge_kutta(f, x[i - 1], y[i - 1], h)

    plt.plot(x, y, label='Runge-Kutta (midpoint) estimation')

    x_exact = np.arange(0, end, 0.01)
    y_exact = 2 * np.exp(x_exact) - x_exact - 1
    plt.plot(x_exact, y_exact, label=r'Exact solution ($y = 2 e^x - x - 1$)')

    plt.legend()
    plt.title(r"""Problem 5.7.1 - 99109393
        Estimating $y' = x + y$ with $h = 0.4$""")
    plt.xlabel('x')
    plt.savefig('plot.png', dpi=600)
    plt.savefig('plot.pdf')
    plt.show()


def q_7_2():
    y = Function('y')
    solution = dsolve(4 * Derivative(y(x), x, x, x, x) + Derivative(y(x), x, x) + 2 * y(x) + 1, y(x))
    print(solution)


if __name__ == '__main__':
    q_7_1()
    q_7_2()
