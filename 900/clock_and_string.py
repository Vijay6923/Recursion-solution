def solve():
    a, b, c, d = map(int, input().split())
    s = ''
    for i in range(1, 13):
        if i == a or i == b:
            s += 'a'
        if i == c or i == d:
            s += 'b'
    if s == "abab" or s == "baba":
        print("YES")
    else:
        print("NO")

def main():
    tt = int(input())
    for _ in range(tt):
        solve()

if __name__ == "__main__":
    main()