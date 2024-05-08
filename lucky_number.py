n = int(input())
lucky_count = 0
while n > 0:
    digit = n % 10
    if digit == 4 or digit == 7:
        lucky_count += 1
    n //= 10
is_lucky = lucky_count == 4 or lucky_count == 7
if is_lucky:
    print("YES")
else:
    print("NO")
