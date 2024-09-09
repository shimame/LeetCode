H, W = [int(x) for x in input().split()]
S = list([input() for _ in range(H)])
y, x = [int(x) for x in input().split()]
if S[y][x] == ".":
    S[y] = list(S[y])
    S[y][x] = "#"
    S[y] = "".join(S[y])
elif S[y][x] == "#":
    S[y] = list(S[y])
    S[y][x] = "."
    S[y] = "".join(S[y])
for i in range(H):
    print(S[i])