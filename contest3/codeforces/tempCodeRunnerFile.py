sticks = sorted(map(int, input().split()))
def triangle_type(a, b, c):
    if a + b <= c:
        return "IMPOSSIBLE"
    elif a + b > c:
        return "TRIANGLE"
    else:
        return "SEGMENT"

results = set()
for i in range(3):
    for j in range(i+1, 4):
        for k in range(4):
            if k != i and k != j:
                results.add(triangle_type(sticks[i], sticks[j], sticks[k]))

if "TRIANGLE" in results:
    print("TRIANGLE")
elif "SEGMENT" in results:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
