def change_mark(y, x, S_map, H, W, d):
    if d == "L":
        step = -1
    else:
        step = 1
    
    val_y = 1
    val_x = step
    up_flag = True
    down_flag = True
    
    while 0 <= x + val_x < W:
        # 上側
        if y + val_y < H and S_map[y+val_y][x+val_x] == "*" and up_flag:
            count_y = 1
            count_x = step
            up_flag = False
            while count_y < val_y:
                S_map[y+count_y][x+count_x] = "*"
                count_y += 1
                count_x += step
        # 下側
        if 0 <= y - val_y and S_map[y-val_y][x+val_x] == "*" and down_flag:
            count_y = 1
            count_x = step
            down_flag = False
            while count_y < val_y:
                S_map[y-count_y][x+count_x] = "*"
                count_y += 1
                count_x += step
        val_y += 1
        val_x += step
    return S_map

H, W, Y, X = [int(n) for n in input().split()]
S_map = [list(input()) for _ in range(H)]
S_map[Y][X] = "*"

# 左
S_map = change_mark(Y, X, S_map, H, W, "L") 

# 右
S_map = change_mark(Y, X, S_map, H, W, "R") 

for j in range(H):
    print("".join(S_map[j]))