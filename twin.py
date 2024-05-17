n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
total_sum = sum(coins)
current_sum = 0
num_coins = 0
for coin in coins:
    current_sum += coin
    num_coins += 1
    if current_sum > total_sum - current_sum:
        break
print(num_coins)
