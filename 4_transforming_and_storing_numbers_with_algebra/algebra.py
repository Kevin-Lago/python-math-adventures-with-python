def equation(a: float, b: float, c: float, d: float) -> float:
    """solves equations of the form:
    ax + b = cx + d
    """
    return (d - b) / (a - c)


if __name__ == '__main__':
    print(equation(1/2, 2/3, 1/5, 7/8))
