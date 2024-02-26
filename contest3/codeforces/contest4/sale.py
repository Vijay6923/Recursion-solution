def max_earnings(n, m, prices):
    prices.sort()
    earnings = 0
    
    for i in range(min(m, n)):
        if prices[i] < 0:
            earnings -= prices[i]
    
    return earnings


n, m = map(int, input().split())
prices = list(map(int, input().split()))
print(max_earnings(n, m, prices))


