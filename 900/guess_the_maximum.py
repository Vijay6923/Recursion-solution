def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        mini = max(a[0], a[1])
        for i in range(1, n - 1):
            mini = min(mini, max(a[i], a[i + 1]))
        
        results.append(mini - 1)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()