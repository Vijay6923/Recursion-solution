t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split( ))
    ans=[]
    for i in range(a,b+1):
        x=(a//c)+(b%c)
        ans.append(x)
    print(max(ans))