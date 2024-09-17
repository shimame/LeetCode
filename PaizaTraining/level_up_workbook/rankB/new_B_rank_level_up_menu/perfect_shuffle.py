K = int(input())
trump = []
suit = ["S", "H", "D", "C"]
for i in suit:
    for j in range(1, 14):
        trump.append(i + "_" + str(j))

half = len(trump) // 2
for _ in range(K):
    top_half = trump[:half]
    bottom_half = trump[half:]
    for i in range(len(trump)):
        if i % 2 == 0:
            trump[i] = top_half.pop(0)
        else:
            trump[i] = bottom_half.pop(0)

for i in trump:
    print(i)