H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]
ans = []
for i in range(H):
    if "#" in S[i]:
        for j in range(W):
            if S[i][j] == "#":
                ans.append((i, j))
for y, x in ans:
    print(y, x)