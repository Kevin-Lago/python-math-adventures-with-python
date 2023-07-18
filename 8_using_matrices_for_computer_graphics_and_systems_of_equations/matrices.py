def add_matrices(a: list, b: list) -> list:
    c = [[a[0][0] + b[0][0], a[0][1] + b[0][1], a[1][0] + b[1][0], a[1][1] + b[1][1]]]

    return c


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


def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])

    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(a[j][i])

    return output


if __name__ == '__main__':
    a = [[1, 2, -3, -1]]
    b = [[4, -1], [-2, 3], [6, -3], [1, 0]]
    print(transpose(a))
    print(transpose(b))
