def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1, if any
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2, if any
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array

# Example input
size1 = int(input())
arr1 = list(map(int, input().split()))
size2 = int(input())
arr2 = list(map(int, input().split()))

# Merge the sorted arrays
merged_result = merge_sorted_arrays(arr1, arr2)

# Print the merged sorted array
print(" ".join(map(str, merged_result)))
