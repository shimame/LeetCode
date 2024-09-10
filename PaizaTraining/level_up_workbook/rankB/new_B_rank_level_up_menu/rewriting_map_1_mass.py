H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]
y, x = [int(x) for x in input().split()]
if S[y][x] == ".":
    S[y][x] = "#"
elif S[y][x] == "#":
    S[y][x] = "."
for i in range(H):
    print("".join(S[i]))