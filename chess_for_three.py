def max_draws(p1, p2, p3):
    total_points = p1 + p2 + p3
    if total_points % 2 != 0:
        return -1
    max_games = (p1 + p2 + p3) // 2
    max_draws = min(p1, p2, (total_points - max_games))
 
    if p3 > p1 + p2 + p3 - max_draws:
        return -1

    return max_draws

t = int(input())
for _ in range(t):
    p1, p2, p3 = map(int, input().split())
    print(max_draws(p1, p2, p3))
