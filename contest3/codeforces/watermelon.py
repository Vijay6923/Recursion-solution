def can_divide_watermelon(w):
    if w % 2 == 1:
        return "NO"
    else:
        return "YES"

w = int(input().strip())
result = can_divide_watermelon(w)
print(result)
