def smallest_multiple(n, k):
    m = (n // k) + 1
    multiple = m * k
    return multiple
n, k = map(int,input().split())
print(smallest_multiple(n, k))