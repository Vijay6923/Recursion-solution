def min_moves_to_divisible_by_three(n, arr):
    remainder_counts = [0, 0, 0]
    total_sum = sum(arr)

    for num in arr:
        remainder_counts[num % 3] += 1

    min_moves = 0
    target = total_sum % 3

    if target == 1:
        if remainder_counts[1] >= 1:
            min_moves = 1
        elif remainder_counts[2] >= 2:
            min_moves = 2
        else:
            min_moves = -1
    elif target == 2:
        if remainder_counts[2] >= 1:
            min_moves = 1
        elif remainder_counts[1] >= 2:
            min_moves = 2
        else:
            min_moves = -1

    return min_moves


# Input
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # Output minimum number of moves
    print(min_moves_to_divisible_by_three(n, arr))
