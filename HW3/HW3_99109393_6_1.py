from functools import reduce
import decimal
import numpy as np
import matplotlib.pyplot as plt

decimal.getcontext().prec = 30
# lower if the code took too long to complete

func = {
    1960: 3.2,
    1965: 3.1,
    1970: 3.3,
    1975: 2.4,
    1980: 2.7,
    1985: 1.44,
    1990: 1.52,
    1995: 1.42,
    2000: 1.2,
    2005: 0.87,
}


# Not used
def main1():
    """
    Calculate legendre polynomial using numpy polynomial library.
    This is fast, efficient and gives us the coefficients (instead of numerical values)
    but it has a huge truncation error.

    * Truncation error is because numpy can't use our custom precision set on Decimal types,
    * and because we are calculating the whole polynomial and then evaluating it.
    * This will create big numbers that cancel out each other. So our number is in their lowest digits.

    np.float64 has the highest precision in numpy but still it is not enough.
    (It does not give a correct output on our initial points.)

    Not used for our example but works fine on small numbers like f[1:7] = 10, 20, 3, 15, 1000, 60, 16
    """

    legendre = sum(map(lambda x: (
        pol := reduce((lambda p1, p2: p1 * p2),
                      map(lambda y: np.poly1d([np.float64(1), -y]), (l := list(func), l.remove(x))[0])),
        pol / np.polyval(pol, x) * func[x]  # lambda return statement
    )[-1], func))

    print(legendre)


def legendre_val(x):
    x = decimal.Decimal(x)
    val = decimal.Decimal(0)

    for x1 in func:
        term = decimal.Decimal(1)
        others = list(func)
        others.remove(x1)

        for x2 in others:
            term *= (x - x2) / (x1 - x2)

        val += term * decimal.Decimal(func[x1])

    return val


def main():
    t = np.arange(1959.9, 2005.4, 0.05)
    # I've added a little extrapolation to make 1960 and 2005 visible on the plot
    y = np.array([float(legendre_val(float(xi))) for xi in t])

    f = plt.figure()
    plt.title('Population growth')
    plt.suptitle('My title')
    plt.xlabel('year')
    plt.ylabel('growth')
    plt.suptitle('Numerical Methods - 99109393 HW3', fontsize=6)
    plt.title('Population growth', fontsize=14)
    plt.grid()

    plt.xticks(np.arange(round(min(t), 0), max(t) + 1, 5.0))
    plt.yticks(np.arange(round(min(y), 1), max(y) + 1, 0.5))
    plt.plot(t, y)

    t_marked = [1972, 1999]
    y_marked = [legendre_val(1972), legendre_val(1999)]
    plt.plot(t_marked, y_marked, 'o')

    for t_i, y_i in zip(t_marked, y_marked):
        annot = f'(year = {t_i}, growth = {round(y_i, 2)})'
        plt.annotate(annot, (t_i, y_i), xytext=(-60, -22), textcoords='offset points', fontsize=8)
        print(annot)

    # (year = 1972, growth = 2.52)
    # (year = 1999, growth = 0.70)

    plt.show()

    f.savefig("plot.pdf")
    f.savefig("plot.png", dpi=600)


if __name__ == "__main__":
    main()
