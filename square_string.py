
t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n % 2 != 0:
        print("NO")
    else:
        mid = n // 2
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")
