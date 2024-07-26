t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    count = 0
    for a in range(1, x - 1):
        for b in range(1, x - a):
            max_c = min(x - a - b, (n - a * b) // (a + b))
            if max_c > 0:
                count += max_c
                
    print(count)