def change_diagonal_mark(y, x, S_map, H, W, d):
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
        if y + val_y < H and S_map[y+val_y][x+val_x] != "." and up_flag:
            up_flag = False
            if S_map[y+val_y][x+val_x] == "*":
                count_y = 1
                count_x = step
                while count_y < val_y:
                    S_map[y+count_y][x+count_x] = "*"
                    count_y += 1
                    count_x += step
        # 下側
        if 0 <= y - val_y and S_map[y-val_y][x+val_x] != "." and down_flag:
            down_flag = False
            if S_map[y-val_y][x+val_x] == "*":
                count_y = 1
                count_x = step
                while count_y < val_y:
                    S_map[y-count_y][x+count_x] = "*"
                    count_y += 1
                    count_x += step
        val_y += 1
        val_x += step
    return S_map

def change_row_mark(row, x, w, d):
    if d == "L":
        step = -1
    else:
        step = 1
    now_x = x + step
    while 0 <= now_x < w :
        if row[now_x] == "#":
            break
        if row[now_x] == "*":
            if d == "L":
                row[now_x:x] = "*" * (x - now_x)
            else:
                row[x:now_x] = "*" * (now_x - x)
            break
        now_x += step
    return row


H, W, N = [int(n) for n in input().split()]
S_map = [list(input()) for _ in range(H)]
for _ in range(N):
    Y, X = [int(n) for n in input().split()]

    # 左側斜め
    S_map = change_diagonal_mark(Y, X, S_map, H, W, "L")

    # 右側斜め
    S_map = change_diagonal_mark(Y, X, S_map, H, W, "R")

    # 左
    S_map[Y] = change_row_mark(S_map[Y], X, W, "L") 

    # 右
    S_map[Y] = change_row_mark(S_map[Y], X, W, "R")

    # 転置
    t_S_map = list(map(list, zip(*S_map)))

    # 上
    t_S_map[X] = change_row_mark(list(t_S_map[X]), Y, H, "L")

    # 下
    t_S_map[X] = change_row_mark(list(t_S_map[X]), Y, H, "R")

    S_map = list(map(list, (zip(*t_S_map))))
    S_map[Y][X] = "*"

for j in range(H):
    print("".join(S_map[j]))