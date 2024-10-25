H, W = [int(x) for x in input().split()]
S_map = [list(input()) for _ in range(H)]
ans = []
for y in range(H):
    for x in range(W):
        # 上端
        if y == 0:
            if S_map[y+1][x] == "#":
                ans.append((y, x))
        # 下端
        elif y == H - 1:
            if S_map[y-1][x] == "#":
                ans.append((y, x))
        # 中
        else:
            if S_map[y-1][x] == "#" and S_map[y+1][x] == "#":
                ans.append((y, x))
for y, x in ans:
    print(y, x)