# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def generate_alternate_primes(N):
#     primes = []
#     num = 2
#     while len(primes) < N:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes[::2]

# def main():
#     N = int(input("Enter the number of alternate prime numbers to generate: "))
#     alternate_primes = generate_alternate_primes(N)
#     print("First", N, "alternate prime numbers are:", ' '.join(map(str, alternate_primes)))

# if __name__ == "__main__":
#     main()
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_alternate_primes(N):
    primes = []
    num = 2
    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[::2]

def main():
    N = int(input("Enter the value of N: "))
    alternate_primes = generate_alternate_primes(N)
    print("First", N, "alternate prime numbers are:", ' '.join(map(str, alternate_primes)))

if __name__ == "__main__":
    main()
