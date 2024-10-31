x, y, n = [int(i) for i in input().split()]
compass = ["N", "E", "S", "W"]
count = 0
now_direction = 0
for _ in range(n):
    d = input() # L or R
    if d == "L":
        now_direction = (now_direction - 1) % 4
    elif d == "R":
        now_direction = (now_direction + 1) % 4
    if compass[now_direction] == "N":
        y -= 1
    elif compass[now_direction] == "E":
        x += 1
    elif compass[now_direction] == "S":
        y += 1
    elif compass[now_direction] == "W":
        x -= 1
    print(x, y)