from matplotlib import pyplot as plt
import numpy
from polynomials import quad
from algebra import quadratic_equation


def plot_cubic(a: float, b: float, c: float, d: float) -> None:
    x = numpy.arange(-6.0, 3.0, 0.05)
    y = [(a*i**3 + b*i**2 + c*i + d) for i in x]

    plt.plot(x, y, label='cubic')
    plt.grid(True)
    plt.show()
    plt.close()


def plot_quadratic(a: float, b: float, c: float) -> None:
    x = [i for i in range(-100, 100)]
    y = [quadratic_equation(a, b, c, i) for i in x]

    plt.plot(x, y, label='quadratic')
    plt.grid(True)
    plt.show()
    plt.close()


if __name__ == '__main__':
    plot_cubic(6, 31, 3, -10)
    plot_quadratic(1, 7, 15)
    # plot_polynomial(1/2, 2/3, 1/5, 7/8)
