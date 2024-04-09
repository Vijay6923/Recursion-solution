def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def probability_of_dot_winning(Y, W):
    max_roll = max(Y, W)
    favorable_outcomes = 6 - max_roll + 1  
    total_outcomes = 6

    common_divisor = gcd(favorable_outcomes, total_outcomes)
    return (favorable_outcomes // common_divisor, total_outcomes // common_divisor)
Y, W = map(int, input().split())

result = probability_of_dot_winning(Y, W)
if result[1] == 1:
    print(f"{result[0]}/1")
else:
    print(f"{result[0]}/{result[1]}")
