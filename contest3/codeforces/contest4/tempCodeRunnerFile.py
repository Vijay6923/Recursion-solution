def max_earnings(n, m, prices):
    prices.sort()  
    max_earnings = 0

    if m <= n // 2:
        
        for i in range(m):
            if prices[i] < 0:
                max_earnings -= prices[i]  
    else:
        
        for i in range(n - 1, n - m - 1, -1):
            if prices[i] < 0:
                max_earnings -= prices[i]  

    return max_earnings
n, m = map(int, input().split())
prices = list(map(int, input().split()))
print(max_earnings(n, m, prices))
