def filling_in_nums_upper_right(H, W):
    l_map = [[0 for _ in range(W)] for _ in range(H)]
    start_position = []
    l_map[0][0] = 1

    # 一番左の縦列を埋める
    add_rnum = 1
    for i in range(1, H):
        l_map[i][0] = l_map[i-1][0] + add_rnum
        start_position.append((i, 0))
        if add_rnum < W:
            add_rnum += 1

    # 一番下の行を埋める
    add_wnum = W
    for j in range(1, W):
        if add_wnum < H:
            num = add_wnum
        else:
            num = H
        l_map[H-1][j] = l_map[H-1][j-1] + num
        start_position.append((H-1, j))
        add_wnum -= 1

    # 一番左,下の列から右上に数を埋めていく
    for row, col in start_position:
        while row > 0 and col < W - 1:
            l_map[row-1][col+1] = l_map[row][col] + 1
            row -= 1
            col += 1
    return l_map

def filling_in_nums_row(H, W):
    l_map = [[0 for _ in range(W)] for _ in range(H)]
    num = 1
    for i in range(H):
        for j in range(W):
            l_map[i][j] = num
            num += 1
    return l_map

H, W, D = [int(x) for x in input().split()]
# 右上
if D == 1:
    l_map = filling_in_nums_upper_right(H, W)
# 右
elif D == 2:
    l_map = filling_in_nums_row(H, W)
# 下
elif D == 3:
    H, W = W, H
    l_map = filling_in_nums_row(H, W)
    l_map = zip(*l_map)
# 左下
elif D == 4:
    H, W = W, H
    l_map = filling_in_nums_upper_right(H, W)
    l_map = zip(*l_map)

for i in l_map:
    print(" ".join(map(str, i)))