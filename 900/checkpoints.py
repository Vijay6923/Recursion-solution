import bisect

def main():
    n, q = map(int, input().split())
    checkpoints = list(map(int, input().split()))
    checkpoints.sort()  
    results = []
    for _ in range(q):
        cmd, k = input().split()
        k = int(k)
        if cmd == "ADD":
            if k not in checkpoints:
                bisect.insort(checkpoints, k)
        elif cmd == "DEL":
            if k in checkpoints:
                checkpoints.remove(k)
        if len(checkpoints) == 0:
            results.append(0)
        else:
            results.append(checkpoints[-1] - checkpoints[0])
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()