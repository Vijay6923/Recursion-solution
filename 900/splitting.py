def solve(test_cases):
    results = []
    for case in test_cases:
        n, array = case
        if n < 3:
            results.append("NO")
        else:
            results.append("YES")
          
            results.append("R" + "B" * (n - 1))
    return results
 
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    test_cases.append((n, array))
 
results = solve(test_cases)
 
for result in results:
    print(result)
