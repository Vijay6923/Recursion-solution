# Function to solve the problem for one test case
def most_frequent_letter(s):
    count_A = s.count('A')
    count_B = s.count('B')
    if count_A > count_B:
        return 'A'
    elif count_B > count_A:
        return 'B'
    else:
        return 'A'  # We can return either 'A' or 'B' if they are equal

# Main function to handle input and output
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        s = input()  # Input string
        result = most_frequent_letter(s)
        print(result)

# Calling the main function
if __name__ == "__main__":
    main()
