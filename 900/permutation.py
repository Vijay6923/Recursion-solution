def generate_max_distance_permutations(N):
    A = list(range(1, N+1))
    B = list(range(N, 0, -1))
    return A, B
T = int(input())
for _ in range(T):
    N = int(input())
    A, B = generate_max_distance_permutations(N)
    print(" ".join(map(str, A)))
    print(" ".join(map(str, B)))
