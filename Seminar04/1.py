n = int(input("n = "))
matrix = [[1 for x in range(n)] for x in range(n)]
for x in range(n - 2, -1, -1):
    for y in range(n - 2, -1, -1):
        matrix[x][y] = matrix[x + 1][y] + matrix[x][y + 1]
for line in matrix:
    print(*line)
