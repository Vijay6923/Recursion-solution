import math

def min_screens_needed(x, y):
    screens_for_2x2 = math.ceil(y / 3)
    total_cells = screens_for_2x2 * 15
    used_cells_by_2x2 = y * 4
    remaining_cells = total_cells - used_cells_by_2x2
    
    if remaining_cells >= x:
        return screens_for_2x2
    else:
        x_remaining = x - remaining_cells
        screens_for_1x1 = math.ceil(x_remaining / 15)
        return screens_for_2x2 + screens_for_1x1

t = int(input())
results = []
for _ in range(t):
    x, y = map(int, input().split())
    results.append(min_screens_needed(x, y))

for result in results:
    print(result)
