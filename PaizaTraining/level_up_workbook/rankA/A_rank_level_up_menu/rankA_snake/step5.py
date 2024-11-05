H, W, y, x, N = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]     
compass = ["N", "E", "S", "W"]
now_direction = 0
flag = True
S[y][x] = "*"
for _ in range(N):
    step = 0
    d, l = input().split()

    if d == "L":
        now_direction = (now_direction - 1) % 4
    elif d == "R":
        now_direction = (now_direction + 1) % 4

    while step < int(l) and flag:
        step += 1
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
            S[y][x] = "*"

    if flag == False:
        break

for i in range(H):
    print("".join(S[i]))