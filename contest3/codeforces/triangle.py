sticks = sorted(map(int, input().split()))
if sticks[0] + sticks[1] > sticks[2] or sticks[1] + sticks[2] > sticks[3]:
    print("TRIANGLE")
elif sticks[0] + sticks[1] == sticks[2] or sticks[1] + sticks[2] == sticks[3]:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
