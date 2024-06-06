def smallest_prime_divisor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

def orac_operations(t, queries):
    results = []
    for n, k in queries:
        
        first_addition = smallest_prime_divisor(n)
        n += first_addition
        
        if k > 1:
            n += 2 * (k - 1)
        
        results.append(n)
    return results
t = int(input())
queries = []
for _ in range(t):
    n, k = map(int, input().split())
    queries.append((n, k))


results = orac_operations(t, queries)


for result in results:
    print(result)
