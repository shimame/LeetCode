n = int(input())
cards = list(map(int, input().split()))
cards.sort()
now_max_card = cards[0]
total = 0

for i in range(1, n):
    if abs(cards[i] - cards[i-1]) == 1:
        now_max_card = cards[i]
    else:
        total += now_max_card
        now_max_card = cards[i]
total += cards[-1]
print(total)