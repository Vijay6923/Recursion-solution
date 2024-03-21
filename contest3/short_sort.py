
def can_transform_to_abc(s):
    if s == 'abc':
        return "YES"
    
    if s[0] == 'a' and s[1] == 'c':
        return "YES"
    elif s[0] == 'a' and s[2] == 'b':
        return "YES"
    elif s[1] == 'a' and s[2] == 'c':
        return "YES"
    
    # If none of the above conditions are met, return NO
    return "NO"

# Input number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Input the sequence
    sequence = input().strip()
    # Check if the sequence can be transformed to 'abc' with at most one operation
    result = can_transform_to_abc(sequence)
    # Output the result
    print(result)
