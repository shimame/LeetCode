H, W, N = [int(x) for x in input().split()]
ans = []
S_map = [list(input()) for _ in range(H)]
for _ in range(N):
    y, x = [int(n) for n in input().split()]
    ans.append(S_map[y][x])
for i in ans:
    print(i)