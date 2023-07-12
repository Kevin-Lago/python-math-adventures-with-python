def f(x: float) -> float:
    return 6*x**3 + 31*x**2 + 3*x - 10


def average(a: float, b: float) -> float:
    return (a + b) / 2.0


def guess() -> float:
    lower = -1
    mid_pt = -0.5
    upper = 0

    for i in range(20):
        mid_pt = average(lower, upper)
        if f(mid_pt) == 0:
            return mid_pt
        elif f(mid_pt) < 0:
            upper = mid_pt
        else:
            lower = mid_pt

    return mid_pt


if __name__ == '__main__':
    print(guess())
