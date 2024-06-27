import math

t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().strip().split())
    
    min_ones = float('inf')
    
    for i in range(1, n + 1):
        start_ones = math.ceil(i / k)
        end_ones = math.ceil((n - i + 1) / k)
        total_ones = start_ones + end_ones
        min_ones = min(min_ones, total_ones)
    
    print(min_ones)