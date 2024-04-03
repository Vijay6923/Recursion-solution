# Function to determine the winner for one test case
def determine_winner(n):
    # If n is already divisible by 3, Vanya wins immediately
    if n % 3 == 0:
        return "First"
    
    # If n is not divisible by 3, calculate the number of moves left
    moves_left = 10
    if n % 3 == 1:
        # If n is 4, 7, or any number 1 more than a multiple of 3
        # Vanya will subtract 1, then Vova will add 1 and reach a number divisible by 3 in 9 moves
        moves_left -= 1
    elif n % 3 == 2:
        # If n is 5, 8, or any number 2 more than a multiple of 3
        # Vanya will add 1, Vova will subtract 1, then Vanya will add 1 and reach a number divisible by 3 in 9 moves
        moves_left -= 2
    
    # If moves left is even, Vova wins; if odd, Vanya wins
    if moves_left % 2 == 0:
        return "Second"
    else:
        return "First"

# Main function to handle input and output
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Integer n for current test case
        result = determine_winner(n)
        print(result)

# Calling the main function
if __name__ == "__main__":
    main()
