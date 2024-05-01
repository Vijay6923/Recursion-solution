# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    k=0
    for i in range(1,n+1):
        if(n%i==0):
            k +=1
    if(k==2):
        print("yes")
    else:
        print("no")