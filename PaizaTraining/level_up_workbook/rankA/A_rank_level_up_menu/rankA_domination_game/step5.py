H, W, N = [int(x) for x in input().split()]
S_map = []
for i in range(H):
    input_line = list(input())
    if "*" in input_line:
        now_posi = (i, input_line.index("*"))
    S_map.append(input_line)

l = [int(input()) for _ in range(N)]

change_queue = [(now_posi[0], now_posi[1], 1)]
if 0 in l:
    S_map[now_posi[0]][now_posi[1]] = "?"
while change_queue:
    y, x, count = change_queue.pop(0)
    if count in l:
        chnage_str = "?"
    else:
        chnage_str = "*"
    # 上
    if 0 < y and S_map[y-1][x] == ".":
        S_map[y-1][x] = chnage_str
        change_queue.append((y-1, x, count + 1))
    # 下
    if y < H - 1 and S_map[y+1][x] == ".":
        S_map[y+1][x] = chnage_str
        change_queue.append((y+1, x, count + 1))
    # 左
    if 0 < x and S_map[y][x-1] == ".":
        S_map[y][x-1] = chnage_str
        change_queue.append((y, x-1, count + 1))
    # 右
    if x < W - 1 and S_map[y][x+1] == ".":
        S_map[y][x+1] = chnage_str
        change_queue.append((y, x+1, count + 1))

for j in range(H):
    print("".join(S_map[j]))