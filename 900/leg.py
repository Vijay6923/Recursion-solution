
t = int(input())


for _ in range(t):
    n = int(input())
    cows = n // 4
    remainder = n % 4
    
    if remainder == 0:
        print(cows)
    else:
        print(cows + 1)  # Add 1 chicken for the remainder