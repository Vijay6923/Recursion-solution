n, m = map(int, input().split())
puzzle_sizes = list(map(int, input().split()))


puzzle_sizes.sort()

min_difference = float('inf')

for i in range(m - n + 1):
    current_difference = puzzle_sizes[i + n - 1] - puzzle_sizes[i]
    if current_difference < min_difference:
        min_difference = current_difference

print(min_difference)
