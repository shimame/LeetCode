l = input().split()
H, W, sy, sx, d, m = int(l[0]), int(l[1]), int(l[2]), int(l[3]), l[4], l[5]
S = [input() for _ in range(H)]
compass = ["N", "E", "S", "W"]
current_posi = compass.index(d)
if m == "L":
    turn = 3
elif m == "R":
    turn = 1
move = compass[(turn + current_posi) % 4]

if move == "N":
    sy -= 1
elif move == "E":
    sx += 1
elif move == "S":
    sy += 1
elif move == "W":
    sx -= 1

if (sy < 0 or H <= sy) or (sx < 0 or W <= sx) or S[sy][sx] == "#":
    print("No")
else:
    print("Yes")