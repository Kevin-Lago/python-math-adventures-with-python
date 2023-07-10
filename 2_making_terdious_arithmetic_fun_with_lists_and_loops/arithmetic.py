def average(a: int, b: int):
    return (a + b) / 2


def average2(nums: list):
    return sum(nums) / len(nums)


def my_sum(num: int = 1):
    running_sum = 0

    for i in range(1, num + 1):
        running_sum += i

    return running_sum


def my_sum2(num: int = 1):
    running_sum = 0

    for i in range(num):
        running_sum += i ** 2 + 1

    return running_sum


if __name__ == '__main__':
    print(average2([53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]))
