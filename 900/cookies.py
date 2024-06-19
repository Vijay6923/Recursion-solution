def minimum_time_to_distribute_cookies(T, cases):
    results = []
    for N, M in cases:
        R = M % N
        if R == 0:
            results.append(0)
        else:
            # Calculate how many to destroy or create to make M a multiple of N
            results.append(min(R, N - R))
    return results

# Read input
T = int(input().strip())
cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = minimum_time_to_distribute_cookies(T, cases)

# Print results
print("\n".join(map(str, results)))