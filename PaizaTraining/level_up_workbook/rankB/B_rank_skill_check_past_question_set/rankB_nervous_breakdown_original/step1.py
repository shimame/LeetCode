H, W, N = [int(x) for x in input().split()]
trump_cards = []
for i in range(H):
    cards = input().split()
    trump_cards.append(cards)
L = int(input())
j = 0
remove_count = [0] * N
cont = 0
while len(trump_cards) > 0 and j < L:
    y_1, x_1, y_2, x_2 = [int(k) - 1 for k in input().split()]
    # 判定
    if trump_cards[y_1][x_1] == trump_cards[y_2][x_2]:
        trump_cards[y_1][x_1], trump_cards[y_2][x_2] = 0, 0
        remove_count[j % N - cont] += 2
        cont += 1
    j += 1
for k in remove_count:
    print(k)