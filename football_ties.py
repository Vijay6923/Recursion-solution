t=int(input())
for _ in range(t):
    x, y=map(int,input().split())
    if(x%3==0 and y%3==0):
        print("0")
    else:
        a=x%3
        b=y%3

        print(min(a,b))