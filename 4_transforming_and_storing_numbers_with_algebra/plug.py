def plug() -> int:
    x = -100

    while x < 100:
        if 2 * x + 5 == 13:
            return x
        x += 1


if __name__ == '__main__':
    print(plug())
