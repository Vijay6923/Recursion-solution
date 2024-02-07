def fibonacci(x):
    if x<1:
        return 0
    if x==1:
        return 1
    else:
        return fibonacci(x-2)+fibonacci(x-1)
n=int(input("enter the number: "))
ans=fibonacci(n)
print(ans)