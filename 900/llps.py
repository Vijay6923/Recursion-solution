s = input()
max_char = max(s)
occur = [ch for ch in s if ch == max_char]
palindrome = ''.join(occur)
print(palindrome)
