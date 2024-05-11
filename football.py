s = input().strip()
count = 1
prev = s[0]
for i in range(1, len(s)):
    if s[i] == prev:
        count += 1
        if count >= 7:
            print("YES")
            break
    else:
        count = 1
        prev = s[i]
else:
    print("NO")