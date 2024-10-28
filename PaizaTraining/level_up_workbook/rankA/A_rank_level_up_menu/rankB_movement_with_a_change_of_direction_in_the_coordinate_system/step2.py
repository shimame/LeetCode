def moving(cp, m):
    sy, sx = cp[0], cp[1]
    if m == "N":
        sy -= 1
    elif m == "E":
        sx += 1
    elif m == "S":
        sy += 1
    elif m == "W":
        sx -= 1
    return (sy, sx)

Y, X, N = [int(n) for n in input().split()]
ans = []
cp = (Y, X)
for _ in range(N):
    m = input()
    cp = moving(cp, m)
    ans.append(cp)
for y, x in ans:
    print(y, x)