def power(a, b, m):
    if b == 0:
        return 1 % m
    else:
        return (a * power(a, b - 1, m)) % m
    
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
m = int(input("Enter the value of m: "))
ans = power(a, b, m)
print(ans)
