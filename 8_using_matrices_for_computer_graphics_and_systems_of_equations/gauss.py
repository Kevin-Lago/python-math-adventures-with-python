def gauss(a: list) -> list:
    m = len(a)
    n = len(a[0])

    for j, row in enumerate(a):
        if row[j] != 0:
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor

        for i in range(m):
            if i != j:
                addinv = -1*a[i][j]

                for ind in range(n):
                    a[i][ind] += addinv*a[j][ind]

    return a


if __name__ == '__main__':
    a = [
        [2, -1, 5, 1, -3],
        [3, 2, 2, -6, -32],
        [1, 3, 3, -1, -47],
        [5, -2, -3, 3, 49]
    ]

    print(gauss(a))
