def find_B_and_C(A):
    B = 2 * A
    C = B * A
    return B, C

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    A = int(input())
    B, C = find_B_and_C(A)
    print(B, C)
