n, k = [int(x) for x in input().split()]
prices = [[int(y) for y in input().split()] for _ in range(n)]
t_prices = list(map(list, zip(*prices)))
stores = []

for i in range(k):
    posi = t_prices[i].index(min(t_prices[i]))
    if posi not in stores:
        stores.append(posi)

print(len(stores))