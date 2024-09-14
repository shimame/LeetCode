H, W = [int(x) for x in input().split()]
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

# 一番左の列から右上に数を埋めていく
for row, col in start_position:
    while row > 0 and col < W - 1:
        l_map[row-1][col+1] = l_map[row][col] + 1
        row -= 1
        col += 1
    
for i in l_map:
    print(" ".join(map(str, i)))