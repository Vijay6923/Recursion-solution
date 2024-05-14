a,b,c,d=map(int,input().split( ))
s={a,b,c,d}
k=set(s)
ans=4-len(k)
print(ans)