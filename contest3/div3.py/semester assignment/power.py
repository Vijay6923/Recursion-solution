def power_mod(a, b, m):
    result = 1
    a = a % m  # Take modulo of a with m to handle large 'a'
    
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result

def main():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    m = int(input("Enter value of m: "))

    result = power_mod(a, b, m)
    print(f"The result of ({a}^{b} % {m}) is:", result)

if __name__ == "__main__":
    main()
