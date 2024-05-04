s = input()
digits = [int(char) for char in s if char.isdigit()]
digits.sort()
new_sum = '+'.join(map(str, digits))
print(new_sum)
