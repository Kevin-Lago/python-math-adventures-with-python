import sys


def average(a: int, b: int) -> float:
    return (a + b) / 2


def square_root(num, low, high) -> float:
    for i in range(20):
        guess = average(low, high)
        if guess ** 2 == num:
            print(guess)
        elif guess ** 2 > num:
            high = guess
        else:
            low = guess
        print(guess)


if __name__ == '__main__':
    print(sys.maxsize)
    square_root(60, 7, 8)
