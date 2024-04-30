matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_index = i
            col_index = j
            break
row_moves = abs(row_index - 2)
col_moves = abs(col_index - 2)
print(row_moves + col_moves)
