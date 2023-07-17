from math import sqrt


def c_add(a: list, b: list) -> list:
    return [a[0]+b[0], a[1]+b[1]]


def c_mult(u: list, v: list) -> list:
    return [u[0]*v[0]-u[1]*v[1], u[1]*v[0]+u[0]*v[1]]


def magnitude(z: list) -> float:
    return sqrt(z[0]**2 + z[1]**2)


if __name__ == '__main__':
    z = [0.25, 0.75]
    z2 = c_mult(z, z)
    z3 = c_add(z, z2)
    m = magnitude(z3)
    print(m)
