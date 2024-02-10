
def conditions(n, a, b):
    if a[-1] == max(a) and b[-1] == max(b):
        return "No"
    else:
        return "Yes"
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    ans = conditions(n, a, b)
    print(ans)
