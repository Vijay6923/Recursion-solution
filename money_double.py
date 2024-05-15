t=int(input())
for _ in range(t):
    x, y=map(int,input().split())
    a=((x+1000)*y)
    b=(x*(2**y))
    print(max(a,b))