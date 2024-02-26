def most_frequent_char(s):
    count_a = s.count('𝙰')
    count_b = s.count('𝙱')
    if count_a > count_b:
        return '𝙰'
    elif count_b > count_a:
        return '𝙱'
    else:
        return '𝙰'

t = int(input())


for _ in range(t):
    s = input()
    result = most_frequent_char(s)
    print(result)
