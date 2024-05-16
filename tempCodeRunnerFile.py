def is_representable(n):
    for x in range(n // 2020 + 1):
        if (n - 2020 * x) % 2021 == 0:
            return "YES"
    return "NO"
t = int(input())
for _ in range(t):
    n = int(input())
    print(is_representable(n))
