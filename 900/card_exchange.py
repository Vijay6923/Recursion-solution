t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))
    card_counts = {}
    ans = n
    for card in cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
 
        if card_counts[card] >= k:
            ans = k - 1
            break
 
    print(ans)