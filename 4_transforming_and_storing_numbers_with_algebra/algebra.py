def first_degree_equation(a: float, b: float, c: float, d: float) -> float:
    """solves equations of the form:
    ax + b = cx + d
    """
    return (d - b) / (a - c)


def quadratic_equation(a: float, b: float, c: float, x: float) -> float:
    return a*x**2 + b*x + c


def cubic_equation(x: float, a: float, b: float, c: float, d: float) -> float:
    return a*x**3 + b*x**2 + c*x + d


if __name__ == '__main__':
    print(first_degree_equation(1/2, 2/3, 1/5, 7/8))
