def change_row(row, x, w, d):
    if d == "L":
        step = -1
    else:
        step = 1
    now_x = x + step
    while 0 <= now_x < w :
        if row[now_x] == "*":
            if d == "L":
                row[now_x:x] = "*" * (x - now_x)
            else:
                row[x:now_x] = "*" * (now_x - x)
            break
        now_x += step
    return row
 
H, W, Y, X = [int(n) for n in input().split()]
S_map = [list(input()) for _ in range(H)]
S_map[Y][X] = "*"

# 左
S_map[Y] = change_row(S_map[Y], X, W, "L") 

# 右
S_map[Y] = change_row(S_map[Y], X, W, "R")

t_S_map = list(zip(*S_map))

# 上
t_S_map[X] = change_row(list(t_S_map[X]), Y, H, "L")

# 下
t_S_map[X] = change_row(list(t_S_map[X]), Y, H, "R")

S_map = list(zip(*t_S_map))

for j in range(H):
    print("".join(S_map[j]))