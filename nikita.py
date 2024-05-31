t=int(input())
for _ in range(t):
    n, m=map(int,input().split())
    if(n>=m and n%2==m%2):
        print("yes")
    else:
        print("no")