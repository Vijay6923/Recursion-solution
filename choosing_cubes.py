t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    favorite_value = a[f - 1]
    sorted_a = sorted(a, reverse=True)
    count_favorite_value = sorted_a.count(favorite_value)
    first_occurrence = sorted_a.index(favorite_value)
    last_occurrence = first_occurrence + count_favorite_value - 1
    if last_occurrence < k:
        print("YES")
    elif first_occurrence >= k:
        print("NO")
    else:
        print("MAYBE")


