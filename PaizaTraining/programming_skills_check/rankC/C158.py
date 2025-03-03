n, m = map(int, input().split())
merchandises = [list(map(int, input().split())) for _ in range(n)]
total_price = sum(x[1] for x in merchandises) * 85 // 100
current_price = 0
item_count = 0

for i in range(1, m):
    for f, p in merchandises:
        if i % f == 0:
            current_price += p
            item_count += 1

    if item_count >= 3:
        discount_rate = 15
    elif item_count >= 2:
        discount_rate = 10
    else:
        discount_rate = 0
    
    total_price += current_price * (100 - discount_rate) // 100
    current_price, item_count = 0, 0

print(total_price)