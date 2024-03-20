import math

def largest_divisor_not_self(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return max(i, n // i)
    return n

def position_of_one(n):
    if n == 1:
        return 1
    largest_non_self_divisor = largest_divisor_not_self(n)
    return n // largest_non_self_divisor

def main():
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        n = int(input())
        print(position_of_one(n))

if __name__ == "__main__":
    main()
