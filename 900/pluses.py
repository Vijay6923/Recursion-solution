def max_bananas(t, test_cases):
    results = []
    
    for case in test_cases:
        a, b, c = sorted(case)
        increments = 5
        
        while increments > 0:
            if a <= b and a <= c:
                a += 1
            elif b <= a and b <= c:
                b += 1 
            else:
                c += 1
            increments -= 1
        
        results.append(a * b * c)
    
    return results
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = max_bananas(t, test_cases)

for result in results:
    print(result)