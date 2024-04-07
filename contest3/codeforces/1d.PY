# Function to calculate the minimum number of operations needed to remove all black cells
def min_operations(n, k, s):
    operations = 0
    i = 0
    while i < n:
        if s[i] == 'B':
            operations += 1
            i += k
        else:
            i += 1
    return operations

# Main function
if __name__ == "__main__":
    # Input number of test cases
    t = int(input())
    
    # Iterate through each test case
    for _ in range(t):
        # Input parameters for the test case
        n, k = map(int, input().split())
        s = input().strip()
        
        # Calculate and output the minimum number of operations needed
        print(min_operations(n, k, s))
