n, l = [int(x) for x in input().split()]
prices = [int(i) for i in input().split()]
if max(prices) >= l:
    posi = prices.index(max(prices))
    prices[posi] = int(max(prices) / 2)
print(sum(prices))