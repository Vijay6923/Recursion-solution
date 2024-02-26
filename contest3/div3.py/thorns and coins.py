def max_coins_helper(n, path, memo, idx):
    if idx >= n:
        return 0
    if memo[idx] != -1:
        return memo[idx]
    
    if path[idx] == '*':
        memo[idx] = max_coins_helper(n, path, memo, idx + 1)
    else:
        # Try moving one step and two steps
        one_step = (1 if path[idx] == '@' else 0) + max_coins_helper(n, path, memo, idx + 1)
        two_steps = (1 if path[idx] == '@' else 0) + max_coins_helper(n, path, memo, idx + 2)
        memo[idx] = max(one_step, two_steps)
    
    return memo[idx]

def max_coins(n, path):
    memo = [-1] * n
    return max_coins_helper(n, path, memo, 0)

# Input number of test cases
t = int(input().strip())

# Iterate through each test case
for _ in range(t):
    # Input length of the path and the description of the path
    n = int(input().strip())
    path = input().strip()

    # Output the maximum number of coins you can collect
    print(max_coins(n, path))
