x, y, a, b = map(int, input().split())
store = []
for i in range(a, x + 1):
    for j in range(b, y + 1):
        if i > j:
            store.append((i, j))
print(len(store))
for i in store:
    print(i[0], i[1])

