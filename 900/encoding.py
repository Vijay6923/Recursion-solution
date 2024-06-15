def solve(n, b):
    cnt = [0] * 26
    for c in b:
        cnt[ord(c) - ord('a')] = 1
    tmp = ''
    for i in range(26):
        if cnt[i] > 0:
            tmp += chr(ord('a') + i)
    a = ''
    for c in b:
        a += tmp[-1 - tmp.find(c)]
    return a

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        b = input().strip()
        result = solve(n, b)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
