def solve():
    s = input()
    if s[0] != '-':
        print(s)
    else:
        i = 1
        while i < len(s):
            if s[i] == '0':
                s = s[:i] + s[i+1:]
            else:
                break
        sz = len(s) - 1
        if s[sz-1] > s[sz]:
            s = s[:sz-1] + s[sz:]
            if s == "-0":
                print(0)
            else:
                print(s)
        else:
            s = s[:-1]
            print(s)

def main():
    TC = 1
    while TC > 0:
        solve()
        TC -= 1

if __name__ == "__main__":
    main()
