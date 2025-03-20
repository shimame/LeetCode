price, discount_rate = map(int, input().split())
total = 0
while price > 0:
    total += price
    price = price * (100 - discount_rate) // 100
print(total)