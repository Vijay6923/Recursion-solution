def sum_of_n_with_largest_divisor_k(T, test_cases):
    results = []
    for K in test_cases:
        total_sum = 0
        for m in range(2, 10**12 // K + 1):
            N = K * m
            if K == max(d for d in range(1, int(N**0.5) + 1) if N % d == 0 and d != N):
                total_sum += N
            if total_sum > 10**18:  
                break
        results.append(total_sum)
    return results

T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]
results = sum_of_n_with_largest_divisor_k(T, test_cases)
for result in results:
    print(result)