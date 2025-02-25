n, m = map(int, input().split())
cards = [int(input()) for _ in range(n)]
card_kinds = []

for i in range(n):
    if cards[i] not in card_kinds:
        card_kinds.append(cards[i])
        if len(card_kinds) == m:
            break

if len(card_kinds) == m:
    print(i+1)
else:
    print("unlucky")