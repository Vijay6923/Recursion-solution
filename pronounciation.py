# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    ans=0
    for i in range(n):
        if(s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u'):
            c=c+1
        else:
            if(c>=4):
                ans=1
                break
            c=0
    if(c>=4):
        ans=1

    if(ans!=1):
        print("YES")
    else:
        print("NO")