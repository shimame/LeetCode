H, W = [int(x) for x in input().split()]
S_map = []
for i in range(H):
    input_line = list(input())
    if "*" in input_line:
        now_posi = (i, input_line.index("*"))
    S_map.append(input_line)

y = now_posi[0]
x = now_posi[1]
if 0 < y:
    S_map[y-1][x] = "*"
if y < H - 1:
    S_map[y+1][x] = "*"
if 0 < x:
    S_map[y][x-1] = "*"
if x < W - 1:
    S_map[y][x+1] = "*"

for j in range(H):
    print("".join(S_map[j]))