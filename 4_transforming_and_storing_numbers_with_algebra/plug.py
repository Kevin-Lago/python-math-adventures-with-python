def g(x: float) -> float:
    return 6*x**3 + 31*x**2 + 3*x - 10


def plug() -> int:
    x = -100

    while x < 100:
        if g(x) == 0:
            return x
        x += 1


if __name__ == '__main__':
    print(plug())
