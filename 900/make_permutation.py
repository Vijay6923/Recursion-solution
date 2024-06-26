# cook your dish here
def can_form_permutation(N, A):
    A_sorted = sorted(A)
    used_values = set()
    for i in range(N):
        target = A_sorted[i]
        while target in used_values or target <= 0:
            target += 1
        if target > N:
            return "NO"
        used_values.add(target)
    return "YES"
def process_test_cases(T, test_cases):
    results = []
    for case in test_cases:
        N, A = case
        result = can_form_permutation(N, A)
        results.append(result)
    return results
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))
results = process_test_cases(T, test_cases)
for result in results:
    print(result)
