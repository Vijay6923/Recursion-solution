def minimize_total_distance(test_cases):
    results = []
    for x1, x2, x3 in test_cases:
        points = sorted([x1, x2, x3])
        median = points[1]  
        total_distance = abs(median - points[0]) + abs(median - points[1]) + abs(median - points[2])
        results.append(total_distance)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    x1, x2, x3 = map(int, input().split())
    test_cases.append((x1, x2, x3))
results = minimize_total_distance(test_cases)
for result in results:
    print(result)