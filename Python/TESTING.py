rows = 8
cols = 8

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

matrix = []

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(0)

for i in A:
    matrix[i[0]][i[1]] = 1

for i in matrix:
    print(i)