def rewriting(mass):
    if mass == ".":
        return "#"
    else:
        return "."

H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]
y, x = [int(x) for x in input().split()]

change_masses = [[y, x]]
if y > 0:
    change_masses.append([y-1, x])
if x > 0:
    change_masses.append([y, x-1])
if y < H-1:
    change_masses.append([y+1, x])
if x < W-1:
    change_masses.append([y, x+1])

for i, j in change_masses:
    S[i][j] = rewriting(S[i][j])

for i in range(H):
    print("".join(S[i]))