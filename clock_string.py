t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if (a>c and c<b ) or (c>a and a<d):
        print("yes")
    else:
        print("no")
87