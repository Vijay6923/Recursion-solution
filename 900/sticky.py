def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = [0] * 101
        for _ in range(n):
            x = int(input().strip())
            a[x] += 1
        sum = 0
        for s in a:
            sum += s // 3
        print(sum)

if __name__ == "__main__":
    main()
