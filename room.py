n = int(input())
count = 0
for _ in range(n):
    pi, qi = map(int, input().split())
    if pi + 2 <= qi:
        count += 1
print(count)
