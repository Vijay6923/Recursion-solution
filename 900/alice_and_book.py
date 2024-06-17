def main():
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        
        mx = 0
        for i in range(n - 1):
            mx = max(mx, a[i])
        
        results.append(mx + a[n - 1])
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()