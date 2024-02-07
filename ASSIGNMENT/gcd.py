def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter the number (a): "))
b = int(input("Enter the number (b): "))

ans= gcd(a, b)
print(ans)
