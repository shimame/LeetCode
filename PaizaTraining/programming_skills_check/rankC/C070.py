n = int(input())
cards = [list(input()) for _ in range(n)]
counts = [0] * n

for i in range(n):
    kind = set(cards[i])
    for j in kind:
        if cards[i].count(j) > counts[i]:
            if cards[i].count(j) > 2:
                counts[i] = cards[i].count(j)
            elif cards[i].count(j) == 2:
                counts[i] += 1

for k in range(n):
    if counts[k] == 4:
        print("Four Card")
    elif counts[k] == 3:
        print("Three Card")
    elif counts[k] == 2:
        print("Two Pair")
    elif counts[k] == 1:
        print("One Pair")
    else:
        print("No Pair")