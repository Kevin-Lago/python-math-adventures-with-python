from math import sqrt


def quad(a: float, b: float, c: float) -> tuple:
    """Returns the solution of an equation of the form:
    a*x**2 + b*x + c = 0
    """
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2


if __name__ == '__main__':
    print(quad(2, 7, -15))
