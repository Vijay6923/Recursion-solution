def main():
    t = int(input())  
    for _ in range(t):
        n, a, b = map(int, input().split())  
        if b <= a:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            print((b - k + 1) * n + k * (k - 1) // 2)

if __name__ == "__main__":
    main()