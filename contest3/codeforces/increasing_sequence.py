n, d = map(int, input().split())
sequence = list(map(int, input().split()))

moves = 0
for i in range(1, n):
    if sequence[i] <= sequence[i - 1]:
        diff = (sequence[i - 1] - sequence[i]) // d + 1
        sequence[i] += diff * d
        moves += diff

print(moves)
