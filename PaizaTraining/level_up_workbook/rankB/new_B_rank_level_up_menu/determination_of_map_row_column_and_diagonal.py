def rewriting(mass):
    if mass == ".":
        return "#"
    else:
        return "."

H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]
y, x = [int(x) for x in input().split()]

change_masses = set()

# 上下
for col in range(H):
    change_masses.add((col, x))

# 左右
for row in range(W):
    change_masses.add((y, row))

# 左上
u, l = y - 1, x - 1
while u >= 0 and l >= 0:
    change_masses.add((u, l))
    u -= 1
    l -= 1

# 右上
u, r = y - 1, x + 1
while u >= 0 and r < W:
    change_masses.add((u, r))
    u -= 1
    r += 1

# 左下
d, l = y + 1, x - 1
while d < H and l >= 0:
    change_masses.add((d, l))
    d += 1
    l -= 1

# 右下
d, r = y + 1, x + 1
while d < H and r < W:
    change_masses.add((d, r))
    d += 1
    r += 1

for i, j in change_masses:
    S[i][j] = rewriting(S[i][j])

for row in S:
    print("".join(row))