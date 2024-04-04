def min_moves_to_make_students_happy(n, chairs):
    swaps = 0
    students = {i: chairs[i - 1] for i in range(1, n + 1)}  # Create a dictionary to represent students and their chairs

    for i in range(1, n + 1):
        if students[i] == i:  # If a student's number matches their chair number, they are unhappy and need a swap
            j = i % n + 1  # Find another student to swap chairs with
            while students[j] == j:  # Find the next student who is unhappy
                j = j % n + 1
            # Perform the swap
            students[i], students[j] = students[j], students[i]
            swaps += 1

    return swaps

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of students
    n = int(input())
    # Read the initial chair positions of students
    chairs = list(map(int, input().split()))

    # Calculate and print the minimum number of moves required
    print(min_moves_to_make_students_happy(n, chairs))
