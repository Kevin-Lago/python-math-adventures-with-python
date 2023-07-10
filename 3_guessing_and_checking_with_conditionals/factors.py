def factors(num: int) -> list:
    factor_list = []

    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)

    return factor_list


def greatest_common_factor(a: int, b: int) -> tuple:
    a_factor_list = factors(a)
    b_factor_list = factors(b)

    for i in range(a):
        item = a_factor_list[len(a_factor_list) - i - 1]

        if item in b_factor_list:
            return item


if __name__ == '__main__':
    print(greatest_common_factor(150, 138))
