n = int(input())
s = input().split()
user_prices = {}
for i in range(n):
    user_prices[s[i]] = 0

m = int(input())

for _ in range(m):
    name, price = input().split()
    price = int(price)
    user_prices[name] += price
users = sorted(user_prices.items(), key=lambda x: x[1], reverse=True)

for name, price in users:
    print(name)