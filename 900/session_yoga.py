def maximize_earnings(T, cases):
    results = []
    for case in cases:
        N, X, Y = case
        if 2 * X >= Y:
            earnings = N * X
        else:
            max_type2_sessions = N // 2
            remaining_hours = N % 2
            earnings = max_type2_sessions * Y + remaining_hours * X
        results.append(earnings)
    return results

T = int(input())
cases = []
for _ in range(T):
    N, X, Y = map(int, input().split())
    cases.append((N, X, Y))
results = maximize_earnings(T, cases)
for result in results:
    print(result)