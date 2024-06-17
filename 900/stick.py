def main():
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        a = [0] * 101
        
        for _ in range(n):
            x = int(input().strip())
            a[x] += 1
        
        sum_triplets = sum(x // 3 for x in a)
        
        print(sum_triplets)

if __name__ == "__main__":
    main()
