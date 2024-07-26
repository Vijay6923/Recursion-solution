s = input()
n = len(s)
min_char = 'z'  
second_min_char = 'z'
char_count = [0] * 26
for char in s:
    index = ord(char) - ord('a')
    char_count[index] += 1
    if char < min_char:
        second_min_char = min_char
        min_char = char
    elif min_char < char < second_min_char:
        second_min_char = char
if char_count[ord(min_char) - ord('a')] > 1:
    ans = min_char * 2
else:
    ans = min_char + second_min_char
print(ans)