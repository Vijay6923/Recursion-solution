def solve():
    n = int(input())
    cnt = 0
    
    while n > 2:
        t = 5
        now = 2
        while n >= t + now:
            now = t + now
            t += 3
        n -= now
        cnt += 1
    
    if n >= 2:
        cnt += 1
    
    print(cnt)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    testcase = int(data[0])
    index = 1
    
    results = []
    for _ in range(testcase):
        n = int(data[index])
        index += 1
        cnt = 0
        
        while n > 2:
            t = 5
            now = 2
            while n >= t + now:
                now = t + now
                t += 3
            n -= now
            cnt += 1
        
        if n >= 2:
            cnt += 1
        
        results.append(cnt)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()