def change_diagonal_mark(y, x, S_map, H, W, d, m):
    if d == "L":
        step = -1
    else:
        step = 1 

    val_y = 1
    val_x = step
    up_flag = True
    down_flag = True
    
    while 0 <= x + val_x < W and (up_flag or down_flag):
        # 上側
        if  y + val_y < H and S_map[y+val_y][x+val_x] == "#" and up_flag:
            up_flag = False
        if y + val_y < H and S_map[y+val_y][x+val_x] == m and up_flag:
            up_flag = False
            if S_map[y+val_y][x+val_x] == m:
                count_y = 1
                count_x = step
                while count_y < val_y:
                    S_map[y+count_y][x+count_x] = m
                    count_y += 1
                    count_x += step
        # 下側
        if 0 <= y - val_y and S_map[y-val_y][x+val_x] == "#" and down_flag:
            down_flag = False
        if 0 <= y - val_y and S_map[y-val_y][x+val_x] == m and down_flag:
            down_flag = False
            if S_map[y-val_y][x+val_x] == m:
                count_y = 1
                count_x = step
                while count_y < val_y:
                    S_map[y-count_y][x+count_x] = m
                    count_y += 1
                    count_x += step
        val_y += 1
        val_x += step
    return S_map

def change_row_mark(row, x, w, d, m):
    if d == "L":
        step = -1
    else:
        step = 1
    now_x = x + step
    while 0 <= now_x < w:
        if row[now_x] == "#":
            break
        if row[now_x] == m:
            if d == "L":
                row[now_x:x] = m * (x - now_x)
            else:
                row[x:now_x] = m * (now_x - x)
            break
        now_x += step
    return row


H, W, N = [int(n) for n in input().split()]
S_map = [list(input()) for _ in range(H)]
for i in range(2*N):

    Y, X = [int(n) for n in input().split()]

    if i % 2 == 0:
        mark = "A"
    else:
        mark = "B"
    
    # 左側斜め
    S_map = change_diagonal_mark(Y, X, S_map, H, W, "L", mark)

    # 右側斜め
    S_map = change_diagonal_mark(Y, X, S_map, H, W, "R", mark)

    # 左
    S_map[Y] = change_row_mark(S_map[Y], X, W, "L", mark) 

    # 右
    S_map[Y] = change_row_mark(S_map[Y], X, W, "R", mark)

    # 転置
    t_S_map = list(map(list, zip(*S_map)))

    # 上
    t_S_map[X] = change_row_mark(list(t_S_map[X]), Y, H, "L", mark)

    # 下
    t_S_map[X] = change_row_mark(list(t_S_map[X]), Y, H, "R", mark)

    S_map = list(map(list, (zip(*t_S_map))))
    S_map[Y][X] = mark

for j in range(H):
    print("".join(S_map[j]))