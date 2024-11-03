def moving(cp, m):
    compass = ["N", "E", "S", "W"]
    now_posi = compass.index(cp[2])
    if m == "L":
        turn = 3
    elif m == "R":
        turn = 1
    move = compass[(turn + now_posi) % 4]
    sy, sx = cp[0], cp[1]
    if move == "N":
        sy -= 1
    elif move == "E":
        sx += 1
    elif move == "S":
        sy += 1
    elif move == "W":
        sx -= 1
    return (sy, sx, move)

H, W, sy, sx, N = [int(x) for x in input().split()]
cp = (sy, sx, "N")
S = [input() for _ in range(H)] # 座標
d = [input() for _ in range(N)] # 移動の向き
ans = []
i = 0
flag = True
while i < N and flag:
    cp = moving(cp, d[i])
    sy, sx = cp[0], cp[1]
    if S[sy][sx] != ".":
        flag = False
    else:
        ans.append((sy, sx))
    i += 1
for y, x in ans:
    print(y, x)
if not flag:
    print("Stop")