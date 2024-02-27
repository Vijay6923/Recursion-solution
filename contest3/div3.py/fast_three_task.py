def min_moves_to_divisible_by_3(t, test_cases):
    results = []
    for _ in range(t):
        n, arr = test_cases[_]
        total_sum = sum(arr)
        remainder = total_sum % 3
        
        if remainder == 0:
            results.append(0)
        else:
            # Count the number of elements with remainder 1 and 2
            count_1 = arr.count(1)
            count_2 = arr.count(2)
            
            if remainder == 1:
                # If the remainder is 1, we need to either remove one element with remainder 1
                # or two elements with remainder 2
                if count_1 >= 1:
                    results.append(1)
                elif count_2 >= 2:
                    results.append(2)
                else:
                    results.append(-1)  # Not possible
            elif remainder == 2:
                # If the remainder is 2, we need to either remove one element with remainder 2
                # or two elements with remainder 1
                if count_2 >= 1:
                    results.append(1)
                elif count_1 >= 2:
                    results.append(2)
                else:
                    results.append(-1)  # Not possible
                
    return results

# Reading input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    test_cases.append((n, arr))

# Getting results
results = min_moves_to_divisible_by_3(t, test_cases)

# Printing results
for res in results:
    print(res)
