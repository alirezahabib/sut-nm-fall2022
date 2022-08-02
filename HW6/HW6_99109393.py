def doolittle(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        L[i][i] = 1
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


def pretty_print(matrix):
    for i in range(n):
        for j in range(n):
            print("{: 9.3f}".format(matrix[i][j]), end=' ')
        print()
    print()


if __name__ == "__main__":
    n = int(input("n = "))
    A = [[0.0] * n for i in range(n)]
    print('Enter rows, values seperated by space or comma, like: "1 -2 1"')
    for i in range(n):
        A[i] = list(map(float, input(f"A[{i}] = ").replace(',', '').split()))

    L, U = doolittle(A)
    print("The L matrix is:")
    pretty_print(L)
    print("The U matrix is:")
    pretty_print(U)
