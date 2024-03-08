def lower_bound(arr, x):
    left, right = 0, len(arr) - 1
    result = len(arr)  # Initialize result to the length of the array
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= x:
            result = mid  # Update result
            right = mid - 1
        else:
            left = mid + 1
            
    return result

def upper_bound(arr, x):
    left, right = 0, len(arr) - 1
    result = len(arr)  # Initialize result to the length of the array
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] > x:
            result = mid  # Update result
            right = mid - 1
        else:
            left = mid + 1
            
    return result

def is_present(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5

print("Lower bound of", x, ":", lower_bound(arr, x))
print("Upper bound of", x, ":", upper_bound(arr, x))
print("Is", x, "present in the array?", is_present(arr, x))
