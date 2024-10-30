def moving(x, y, move):
    if move == "N":
        y -= 1
    elif move == "E":
        x += 1
    elif move == "S":
        y += 1
    elif move == "W":
        x -= 1
    return (x, y)

x, y, n = [int(i) for i in input().split()]
compass = ["N", "E", "S", "W"]
count = 0
now_direction = 1
max_count = 1
first_set = True
for _ in range(n):
    (x, y) = moving(x, y, compass[now_direction])
    count += 1
    if first_set and count == max_count:
        count = 0
        first_set = False
        now_direction = (now_direction + 1) % 4
    elif not first_set and count == max_count:
        count = 0
        max_count += 1
        first_set = True
        now_direction = (now_direction + 1) % 4
print(x, y)