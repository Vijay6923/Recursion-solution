def ispossibletogetoneelement(n, arr):
    arr.sort()
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:
            return "NO"
    return "YES"

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    ans = ispossibletogetoneelement(n, arr)
    print(ans)
