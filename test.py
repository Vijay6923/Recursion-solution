import math
t=int(input())
for _ in range(t):
    x, y=map(int,input().split())
    if (x<=y):
        print(math.ceil(y/2))
    else:
        a=math.ceil(y/2)
        b=(abs((a*15)-(y*4)-x))
        print(a+math.ceil(b/15))