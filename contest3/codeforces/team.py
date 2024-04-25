
n = int(input())
problems_to_implement = 0
for _ in range(n):
    views = list(map(int, input().split()))
    sure_count = sum(views)
    if sure_count >= 2:
        problems_to_implement += 1


print(problems_to_implement)
