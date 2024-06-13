def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        total_sum = 0
        max_value = 0
        ans = 0
        
        for i in range(n):
            total_sum += a[i]
            max_value = max(max_value, a[i])
            if total_sum - max_value == max_value:
                ans += 1
        
        print(ans)

if __name__ == "__main__":
    main()
