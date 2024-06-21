def pow(x, y, m=int(1e9+7)):
    ans = 1
    x %= m
    while y:
        if y & 1:
            ans = (ans * x) % m
        x = (x * x) % m
        y >>= 1
    return ans

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    TCS = int(data[index])
    index += 1
    results = []
    
    for _ in range(TCS):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        v = []
        for i in range(n):
            v.append(data[index])
            index += 1
        
        x, y = 0, 0
        mx, my = 0, 0
        
        # Find the row with the maximum '#'
        for i in range(n):
            ct = v[i].count('#')
            if ct > mx:
                mx = ct
                x = i + 1
        
        # Find the column with the maximum '#'
        for j in range(m):
            ct = sum(1 for i in range(n) if v[i][j] == '#')
            if ct > my:
                my = ct
                y = j + 1
        
        results.append(f"{x} {y}")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
