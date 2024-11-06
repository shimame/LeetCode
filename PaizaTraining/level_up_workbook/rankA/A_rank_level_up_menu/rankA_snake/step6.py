H, W, y, x, N = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]     
compass = ["N", "E", "S", "W"]
now_direction = 0
flag = True
time = 0
for _ in range(N):
    t, d = input().split() # time, direction

    while time < int(t) and flag:
        time += 1
        if compass[now_direction] == "N":
            y -= 1
        elif compass[now_direction] == "E":
            x += 1
        elif compass[now_direction] == "S":
            y += 1
        elif compass[now_direction] == "W":
            x -= 1
        
        if not((0 <= x < W) and (0 <= y < H) and S[y][x] == "."):
            flag = False
        else:
            print(y, x)
    if flag:
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
        if not((0 <= x < W) and (0 <= y < H) and S[y][x] == "."):
            flag = False
        else:
            print(y, x)
        time += 1
    else:
        break

if not flag:
    print("Stop")