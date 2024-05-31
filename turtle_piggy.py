def max_score(l, r):
    power_of_2 = 1
    while power_of_2 * 2 <= r:
        power_of_2 *= 2
    if power_of_2 < l:
        power_of_2 //= 2
    score = 0
    while power_of_2 > 1:
        power_of_2 //= 2
        score += 1
    
    return score

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        l, r = map(int, input().strip().split())
        results.append(max_score(l, r))
    
    for result in results:
        print(result)
if __name__ == "__main__":
    main()
