H, W = [int(x) for x in input().split()]
S_map = []
num_map = [["#" for _ in range(W)] for _ in range(H)]
for i in range(H):
    input_line = list(input())
    if "*" in input_line:
        now_posi = (i, input_line.index("*"))
    S_map.append(input_line)

change_queue = [(now_posi[0], now_posi[1], 0)]
num_map[now_posi[0]][now_posi[1]] = str(0)
while change_queue:
    y, x, count = change_queue.pop(0)

    # 上
    if 0 < y and S_map[y-1][x] == ".":
        S_map[y-1][x] = "*"
        num_map[y-1][x] = str(count + 1)
        change_queue.append((y-1, x, count + 1))
    # 下
    if y < H - 1 and S_map[y+1][x] == ".":
        S_map[y+1][x] = "*"
        num_map[y+1][x] = str(count + 1)
        change_queue.append((y+1, x, count + 1))
    # 左
    if 0 < x and S_map[y][x-1] == ".":
        S_map[y][x-1] = "*"
        num_map[y][x-1] = str(count + 1)
        change_queue.append((y, x-1, count + 1))
    # 右
    if x < W - 1 and S_map[y][x+1] == ".":
        S_map[y][x+1] = "*"
        num_map[y][x+1] = str(count + 1)
        change_queue.append((y, x+1, count + 1))

for j in range(H):
    print("".join(num_map[j]))