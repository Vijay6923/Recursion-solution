t = int(input())
cards = []
h = 1
while True:
    required_cards = h * (3 * h + 1) // 2
    if required_cards > 10**9:
        break
    cards.append(required_cards)
    h += 1

for _ in range(t):
    n = int(input())
    count = 0

    for i in reversed(range(len(cards))):
        count += n // cards[i]
        n %= cards[i]

    print(count)
