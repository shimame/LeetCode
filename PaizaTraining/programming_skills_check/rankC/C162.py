m, n = [int(x) for x in input().split()]
cards = [int(y) + 1 for y in range(m)]
center = m // 2

for _ in range(n):
    low_deck = cards[:center]
    high_deck = cards[center:]
    shuffled_deck = []
    for i in range(center):
        shuffled_deck.append(high_deck.pop(0))
        shuffled_deck.append(low_deck.pop(0))
    cards = shuffled_deck
print(" ".join(map(str, cards)))