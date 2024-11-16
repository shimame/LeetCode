def change_mark(y, x, S_map, H, W, d):
    if d == "L":
        step = -1
    else:
        step = 1
    val = step
    while 0 <= x + val < W:
        if 0 <= y + val < H:
            S_map[y+val][x+val] = "*"
        if 0 <= y - val < H:
            S_map[y-val][x+val] = "*"
        val += step
    return S_map

H, W, Y, X = [int(n) for n in input().split()]
S_map = [["." for _ in range(W)] for _ in range(H)]

# 左側
S_map = change_mark(Y, X, S_map, H, W, "L")
# 右側
S_map = change_mark(Y, X, S_map, H, W, "R")

S_map[Y][X] = "!"

for i in range(H):
    print("".join(S_map[i]))