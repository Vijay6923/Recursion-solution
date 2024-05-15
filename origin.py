T = int(input())
for _ in range(T):
    N = int(input())
    sumoforigins = ((N//9)*45)
    
    for i in range(1, N%9+1):
        origin = i % 9 or 9
        sumoforigins += origin
    
    print(sumoforigins)
