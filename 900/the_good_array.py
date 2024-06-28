def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:]))
    
    maxx = 0
    maxx2 = 0
    total = 0
    mem = []
   
    for j in a:
        total += j
        if j > maxx:
            maxx2 = maxx
            maxx = j
        elif j > maxx2:
            maxx2 = j
    
    checknice = 0
    for i in range(n):
        if a[i] != maxx:
            if maxx == (total - a[i] - maxx):
                mem.append(i + 1)
                checknice += 1
        else:
            if maxx2 == (total - a[i] - maxx2):
                mem.append(i + 1)
                checknice += 1
    
    print(checknice)
    print(' '.join(map(str, mem)))

if __name__ == "__main__":
    main()