# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(input())
    i=0
    temp1=str()
    temp2=str()
    if n%2==0:
        while i<n:
            temp1=temp1+s[i+1]+s[i]
            i=i+2
    else:
        while i<(n-1):
            temp1=temp1+s[i+1]+s[i]
            i=i+2
        temp1 = temp1 + s[n-1]
    #print(ord(temp1[0]))
    i=0
    while i<n:
        temp2=temp2+chr(122+97-ord(temp1[i]))
        i=i+1
    print(temp2)