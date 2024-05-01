# cook your dish here
t=int(input())
for _ in range(t):
    n, k=map(int,input().split())
    N=list(map(int,input().split()))
    count=0
    for i in N:
        if((i+k)%7==0):
            count=count+1
    print(count)