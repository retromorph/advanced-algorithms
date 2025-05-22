def prepend(matrix):
    a1 = [[0] + row for row in matrix]
    a2 = [[0] * (len(matrix[0]) + 1)]
    return a2 + a1

def append(matrix):
    a1 = [row + [0] for row in matrix]
    a2 = [[0] * (len(matrix[0]) + 1)]
    return a1+a2

def max_mex_matrix(n):
    if n == 1:
        return [[0]]

    k = (n - 1)**2

    if n % 2 == 0:
        matrix = append(max_mex_matrix(n - 1))
        for i in range(n - 1):
            matrix[i][n - 1] = k
            k += 1

        for i in range(n):
            matrix[n - 1][i] = k
            k += 1
        return matrix

    matrix = prepend(max_mex_matrix(n - 1))
    for i in range(1, n):
        matrix[0][i] = k
        k += 1

    for i in range(1, n):
        matrix[i][0] = k
        k += 1

    matrix[0][0] = k
    return matrix

Q = int(input())

for _ in range(Q):
    n = int(input())
    M = max_mex_matrix(n)
    for row in M:
        print(' '.join(map(str, row)))