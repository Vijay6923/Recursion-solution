t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input().strip()
    x = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
    for char in a:
        x[char] += 1
    additional_problems = 0
    for level in 'ABCDEFG':
        if x[level] < m:
            additional_problems += (m - x[level])
    print(additional_problems)
