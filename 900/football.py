import math
a, b, c = map(int, input().split())
x = a * c
y = b * c
z = x - y
if z <= 0:
    min_wait_time = 0
else:
    min_wait_time = math.ceil(z / b)
print(min_wait_time)
