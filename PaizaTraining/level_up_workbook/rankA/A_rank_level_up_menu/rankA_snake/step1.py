l = input().split()
H, W, sy, sx, m = int(l[0]), int(l[1]), int(l[2]), int(l[3]), l[4]
S = [input() for _ in range(H)]
if m == "N":
    sy -= 1
elif m == "E":
    sx += 1
elif m == "S":
    sy += 1
elif m == "W":
    sx -= 1

if (sy < 0 or H <= sy) or (sx < 0 or W <= sx) or S[sy][sx] == "#":
    print("No")
else:
    print("Yes")