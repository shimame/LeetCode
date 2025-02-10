n = int(input())
item_prices = list(map(int, input().split()))
had_money, q = map(int, input().split())
for _ in range(q):
    x, k = map(int, input().split())
    if item_prices[x-1] * k <= had_money:
        had_money -= item_prices[x-1] * k
print(had_money)