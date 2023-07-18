A = [[2, 3], [5, -8]]
B = [[1, -4], [8, -6]]


def add_matrices(a: list, b: list) -> list:
    C = [[a[0][0] + b[0][0], a[0][1] + b[0][1], a[1][0] + b[1][0], a[1][1] + b[1][1]]]

    return C


def multiply_matrices(a: list, b: list) -> list:
    m = len(a)
    n = len(b[0])
    new_matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        new_matrix.append(row)
    return new_matrix


if __name__ == '__main__':
    a = [[1, -2], [2, 1]]
    b = [[3, -4], [5, 6]]
    print(multiply_matrices(a, b))
