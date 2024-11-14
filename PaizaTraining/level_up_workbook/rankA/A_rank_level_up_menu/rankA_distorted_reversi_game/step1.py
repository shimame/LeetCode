H, W, Y, X = [int(n) for n in input().split()]
S_map = [["." for _ in range(W)] for _ in range(H)]

S_map[Y] = ["*"] * W
for i in range(H):
    S_map[i][X] = "*"
S_map[Y][X] = "!"

for j in range(H):
    print("".join(S_map[j]))