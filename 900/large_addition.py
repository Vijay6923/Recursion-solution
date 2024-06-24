def solve(n):
    n = n - n % 10 + (n % 10 + 1) % 10
    while n > 9:
        if n % 10 == 0:
            return "NO"
        n //= 10
    
    return "YES" if n == 1 else "NO"
 
def main():
    t = int(input()) 
    results = []
    for _ in range(t):
        n = int(input())
        results.append(solve(n))
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()
