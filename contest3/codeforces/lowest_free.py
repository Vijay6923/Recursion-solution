# cook your dish here
for k in range(int(input())):
    a=list(map(int,input().split()))
    a.remove(min(a))
    for i in range(len(a)-1):
        print(a[i]+a[i+1])