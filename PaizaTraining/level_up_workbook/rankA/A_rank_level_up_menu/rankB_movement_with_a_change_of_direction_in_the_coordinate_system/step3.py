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

Y, X, D = input().split()    
d = input()
cp = (int(Y), int(X), D)
cp = moving(cp, d)
print(cp[0], cp[1])