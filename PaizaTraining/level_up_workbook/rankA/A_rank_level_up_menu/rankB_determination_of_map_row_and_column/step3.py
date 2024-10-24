H, W = [int(x) for x in input().split()]
S_map = [list(input()) for _ in range(H)]
ans = []
for y in range(H):
    for x in range(W):
        # 左端
        if x == 0:
            if S_map[y][x+1] == "#":
                ans.append((y, x))
        # 右端
        elif x == W - 1:
            if S_map[y][x-1] == "#":
                ans.append((y, x))
        # 中
        else:
            if S_map[y][x-1] == "#" and S_map[y][x+1] == "#":
                ans.append((y, x))
for y, x in ans:
    print(y, x)