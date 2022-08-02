n = int(input("n = "))
table = [[0] * n for i in range(n)]
x = [0] * n

for i in range(n):
    x[i] = float(input(f'x[{i}] = '))
    table[i][0] = float(input(f'y[{i}] = '))

for j in range(1, n):
    for i in range(n - j):
        table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

print('\n  x')
for i in range(n):
    print('{:6.2f}'.format(x[i]), end="\t\t")
    for j in range(n - i):
        print('{:6.2f}'.format(table[i][j]), end="\t")
    print()
print()

z = float(input('y(x), x = '))
prod = 1
total = 0

for i in range(n):
    total += table[0][i] * prod
    prod *= z - x[i]

print(total)
