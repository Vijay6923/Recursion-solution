def min_operations_to_not_sorted(n, arr):
    # Check if the array is already not sorted
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)
    
    if arr != sorted_asc and arr != sorted_desc:
        return 0
    
    # Find the first index where the array is not sorted in ascending order
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Perform operation to make the array not sorted
            return 1
    
    # Find the first index where the array is not sorted in descending order
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            # Perform operation to make the array not sorted
            return 1

    # If the array is already not sorted, return 0 operations
    return 0

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the array and the array itself
    n = int(input())
    arr = list(map(int, input().split()))

    # Calculate and print the minimum operations needed to make the array not sorted
    print(min_operations_to_not_sorted(n, arr))
