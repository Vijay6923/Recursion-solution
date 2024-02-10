
def good_pair(n, arr):
    min_val = min(arr)
    max_val = max(arr)
    min_index = arr.index(min_val) + 1
    max_index = arr.index(max_val) + 1
    return min_index, max_index

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    i, j = good_pair(n, arr)
    print(i, j)
