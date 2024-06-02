n = int(input())
p = list(map(int, input().split()))
givers = [0] * n
for i in range(n):
    givers[p[i] - 1] = i + 1
print(" ".join(map(str, givers)))
