import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def apocalypse_year(n, periods):
    lcm_period = periods[0]
    for i in range(1, n):
        lcm_period = lcm(lcm_period, periods[i])
    return lcm_period

# Input reading and processing
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    periods = list(map(int, input().strip().split()))
    print(apocalypse_year(n, periods))
