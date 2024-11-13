H, W = [int(x) for x in input().split()]
N = input() # 先手のプレイヤー名
S_map = []
A_count, B_count = 0, 0

for i in range(H):
    input_line = list(input())
    if "A" in input_line:
        A_posi = (i, input_line.index("A"), "A")
    if "B" in input_line:
        B_posi = (i, input_line.index("B"), "B")
    S_map.append(input_line)

if N == "A":
    change_queue = [A_posi, B_posi]
else:
    change_queue = [B_posi, A_posi]

while change_queue:
    y, x, mark = change_queue.pop(0)

    # 上
    if 0 < y and S_map[y-1][x] == ".":
        S_map[y-1][x] = mark
        change_queue.append((y-1, x, mark))
    # 下
    if y < H - 1 and S_map[y+1][x] == ".":
        S_map[y+1][x] = mark
        change_queue.append((y+1, x, mark))
    # 左
    if 0 < x and S_map[y][x-1] == ".":
        S_map[y][x-1] = mark
        change_queue.append((y, x-1, mark))
    # 右
    if x < W - 1 and S_map[y][x+1] == ".":
        S_map[y][x+1] = mark
        change_queue.append((y, x+1, mark))

for j in range(H):
    A_count += S_map[j].count("A")
    B_count += S_map[j].count("B")

print(A_count, B_count)

if A_count < B_count:
    print("B")
elif A_count > B_count:
    print("A")
else:
    print("DRAW")