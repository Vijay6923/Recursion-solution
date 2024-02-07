def nCrmodm(n, r, m):
    if r == 0 or r == n:
        return 1 % m
    if r == 1:
        return n % m

n = int(input("Enter n: "))
r = int(input("Enter r: "))
m = int(input("Enter m: "))

ans = nCrmodm(n, r, m)
print(ans)
