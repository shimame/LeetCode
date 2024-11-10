H, W = [int(x) for x in input().split()]
S_map = []
for i in range(H):
    input_line = list(input())
    if "*" in input_line:
        now_posi = (i, input_line.index("*"))
    S_map.append(input_line)

change_queue = [(now_posi[0], now_posi[1])]
while change_queue:
    now = change_queue.pop(0)
    y = now[0]
    x = now[1]

    if 0 < y and S_map[y-1][x] == ".":
        S_map[y-1][x] = "*"
        change_queue.append((y-1, x))
    if y < H - 1 and S_map[y+1][x] == ".":
        S_map[y+1][x] = "*"
        change_queue.append((y+1, x))
    if 0 < x and S_map[y][x-1] == ".":
        S_map[y][x-1] = "*"
        change_queue.append((y, x-1))
    if x < W - 1 and S_map[y][x+1] == ".":
        S_map[y][x+1] = "*"
        change_queue.append((y, x+1))

for j in range(H):
    print("".join(S_map[j]))