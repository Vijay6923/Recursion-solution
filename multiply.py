def min_moves_to_one(test_cases):
    results = []
    for n in test_cases:
        moves = 0
        while n != 1:
            if n % 6 == 0:
                n //= 6
                moves += 1
            elif n % 3 == 0:
                n //= 3
                moves += 2  
            else:
                moves = -1
                break
        
        results.append(moves)
    return results
 
 
t = int(input())
test_cases = [int(input()) for _ in range(t)]
 
 
results = min_moves_to_one(test_cases)
 
 
for result in results:
    print(result)