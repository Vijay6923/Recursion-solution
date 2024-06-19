def solve():
    n = int(input())
    vec = list(map(int, input().split()))
    mp = {}
    
    for num in vec:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1
            
    tot = 0
    for count in mp.values():
        tot += count // 3
        
    print(tot)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        vec = list(map(int, data[index:index + n]))
        index += n
        
        mp = {}
        for num in vec:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        tot = sum(count // 3 for count in mp.values())
        results.append(tot)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
