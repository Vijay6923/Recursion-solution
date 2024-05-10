t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if (a < c and c < b and b < d) or (c < a and a < d and d < b):
        print("YES")
    else:
        print("NO")
87