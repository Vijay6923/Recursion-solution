import math

def max_fireworks(t, test_cases):
    result = []
    for case in test_cases:
        a, b, m = case
        lcm = (a * b) // math.gcd(a, b) # Calculate the least common multiple
        interval_a = lcm // a
        interval_b = lcm // b
        fireworks_count = (m // interval_a) + (m // interval_b) + 1
        result.append(fireworks_count)
    return result

# Input
t = int(input())
test_cases = []
for _ in range(t):
    a, b, m = map(int, input().split())
    test_cases.append((a, b, m))

# Output
output = max_fireworks(t, test_cases)
for count in output:
    print(count)
