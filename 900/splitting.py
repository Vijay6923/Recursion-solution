def main():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        
        if a[0] == a[-1]:
            print("NO")
        else:
            print("YES")
            s = ['R'] * n
            s[1] = 'B'
            print(''.join(s))

if __name__ == "__main__":
    main()
