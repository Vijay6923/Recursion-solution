def max_sum_after_operations(t, test_cases):
    results = []
    for _ in range(t):
        n, arr = test_cases[_]
        max_sum = max_so_far = arr[0]
        min_neg_sum = min_neg_so_far = max(0, -arr[0])
        
        for i in range(1, n):
            max_so_far = max(arr[i], max_so_far + arr[i])
            max_sum = max(max_sum, max_so_far)
            
            min_neg_so_far = max(-arr[i], min_neg_so_far - arr[i])
            min_neg_sum = max(min_neg_sum, min_neg_so_far)
        
        results.append(max_sum + min_neg_sum)
    
    return results

# Reading input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    test_cases.append((n, arr))

# Getting results
results = max_sum_after_operations(t, test_cases)

# Printing results
for res in results:
    print(res)
