def max_bananas(t, test_cases):
    results = []
    
    for i in range(t):
        a, b, c = sorted(test_cases[i])
        
        increments = 5
    
        if increments > 0:
            to_increase = min(b - a, increments)
            a += to_increase
            increments -= to_increase
        
        if increments > 0:
            to_increase = min(c - a, increments)
            a += to_increase
            increments -= to_increase
            
        if increments > 0:
            to_increase = min(c - b, increments)
            b += to_increase
            increments -= to_increase
            
        if increments > 0:
            each = increments // 3
            extra = increments % 3
            a += each
            b += each
            c += each
            if extra > 0:
                a += 1
            if extra > 1:
                b += 1
        
        results.append(a * b * c)
    
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = max_bananas(t, test_cases)

for result in results:
    print(result)