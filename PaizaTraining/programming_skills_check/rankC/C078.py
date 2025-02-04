n, c1, c2 = [int(x) for x in input().split()]
profit = 0
stocks = 0

for i in range(n):
    price = int(input())

    if i == n - 1:
        profit += price * stocks
        stocks = 0
        break

    if price <= c1:
        profit -= price
        stocks += 1
    if price >= c2:
        profit += price * stocks
        stocks = 0

print(profit)