t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    prefix_sum = 0
    seen_elements = set()
    good_prefix_count = 0
    for i in range(n):
        prefix_sum += arr[i]
        seen_elements.add(arr[i])
        if prefix_sum % 2 == 0 and (prefix_sum // 2) in seen_elements:
            good_prefix_count += 1
    results.append(good_prefix_count)
for result in results:
    print(result)
