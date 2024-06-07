def can_defeat_all_dragons(s, dragons):
    dragons.sort()
    for x, y in dragons:
        if s > x:
            s += y
        else:
            return "NO"
    return "YES"
s, n = map(int, input().split())
dragons = [tuple(map(int, input().split())) for _ in range(n)]
result = can_defeat_all_dragons(s, dragons)
print(result)
