def min_segment_length(n, s):
    first_black = s.find('B')
    last_black = s.rfind('B')
    if first_black == last_black:
        return 1
    return last_black - first_black + 1

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        print(min_segment_length(n, s))

if __name__ == "__main__":
    main()
