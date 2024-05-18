def longest_non_decreasing_subsegment(n, a):
    max_length = 1
    current_length = 1
    
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    max_length = max(max_length, current_length)
    return max_length
n = int(input())
a = list(map(int, input().split()))
print(longest_non_decreasing_subsegment(n, a))