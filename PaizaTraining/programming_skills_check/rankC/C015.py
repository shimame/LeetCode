n = int(input())
point = 0
for _ in range(n):
    day, price = [x for x in input().split()]
    if "3" in day:
        point += int(price) * 3 // 100
    elif"5" in day:
        point += int(price) * 5 // 100
    else:
        point += int(price) // 100
print(point)