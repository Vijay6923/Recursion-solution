def solve_problem(test_cases):
    results = []
    
    for case in test_cases:
        n, a, b = case
        mismatches = sum(1 for i in range(n) if a[i] > b[i])
        results.append(mismatches)
    
    return results


import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    b = list(map(int, data[index:index + n]))
    index += n
    test_cases.append((n, a, b))


results = solve_problem(test_cases)


for result in results:
    print(result)
