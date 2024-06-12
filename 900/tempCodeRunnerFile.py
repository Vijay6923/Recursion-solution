t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    prefix_sum = 0
    ele = set()
    goodPrefixCount = 0
    for i in range(n):
        prefix_sum += arr[i]
        ele.add(arr[i])
        if prefix_sum % 2 == 0 and (prefix_sum // 2) in ele:
            goodPrefixCount += 1
    results.append(goodPrefixCount)
for i in results:
    print(i)
