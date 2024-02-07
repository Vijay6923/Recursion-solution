def factorial(n):
    if n<0:
        return 0
    if n==1:
        return 1
    if n>1:
        return (n * factorial(n-1))
    
x=int(input("enter the number: "))
ans=factorial(x)
print(ans)

