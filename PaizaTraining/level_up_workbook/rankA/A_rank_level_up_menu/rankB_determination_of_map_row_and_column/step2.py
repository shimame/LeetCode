H, W, N = [int(x) for x in input().split()]
S_map = [list(input()) for _ in range(H)]
for _ in range(N):
    y, x = [int(n) for n in input().split()]
    S_map[y][x] = "#"
for i in S_map:
    print("".join(i))