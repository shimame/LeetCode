H, W, y, x, N = [int(x) for x in input().split()]
S_map = [list(input()) for _ in range(H)]     
dc_time = [input().split() for _ in range(N)]
compass = ["N", "E", "S", "W"]
now_direction = 0
change_count = 0
now_time = 0
S_map[y][x] = "*"

for now_time in range(100):
    # 方向転換
    if change_count < N and str(now_time) == dc_time[change_count][0]:
        if dc_time[change_count][1] == "L":
            now_direction = (now_direction + 3) % 4
        else:
            now_direction = (now_direction + 1) % 4
        change_count += 1

    # 向いている方角に移動
    if compass[now_direction] == "N":
        y -= 1
    elif compass[now_direction] == "E":
        x += 1
    elif compass[now_direction] == "S":
        y += 1
    elif compass[now_direction] == "W":
        x -= 1
        
    if not((0 <= x < W) and (0 <= y < H) and S_map[y][x] == "."):
        break
    else:
        S_map[y][x] = "*"
    
for i in range(H):
    print("".join(S_map[i]))