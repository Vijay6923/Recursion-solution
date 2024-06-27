t = int(input())
for _ in range(t):
    a, b, n, S = map(int, input().split())
    max_n_coins = min(a, S // n)
    remaining = S - max_n_coins * n
    if remaining <= b:
        print("YES")
    else:
        print("NO")
