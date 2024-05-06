def dollars_to_borrow(k, n, w):
    total_cost = sum(i * k for i in range(1, w + 1))
    borrow_amount = max(0, total_cost - n)
    
    return borrow_amount

k, n, w = map(int, input().split())
print(dollars_to_borrow(k, n, w))
