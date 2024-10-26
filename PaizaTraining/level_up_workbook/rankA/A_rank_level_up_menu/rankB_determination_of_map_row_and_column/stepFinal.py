H, W = [int(x) for x in input().split()]
S_map = [list(input()) for _ in range(H)]
for y in range(H):
    for x in range(W):
        flag_x = False
        flag_y = False

        if x == 0 or S_map[y][x - 1] == "#":
            if x == W - 1 or S_map[y][x + 1] == "#":
                flag_x = True

        if y == 0 or S_map[y - 1][x] == "#":
            if y == H - 1 or S_map[y + 1][x] == "#":
                flag_y = True

        if flag_y and flag_x:
            print(y, x)