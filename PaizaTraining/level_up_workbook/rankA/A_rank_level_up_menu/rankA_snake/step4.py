H, W, y, x, N = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]     
compass = ["N", "E", "S", "W"]
now_direction = 0
flag = True
for _ in range(N):
    d, l = input().split()
    step = 0
    
    if d == "L":
        now_direction = (now_direction - 1) % 4
    elif d == "R":
        now_direction = (now_direction + 1) % 4

    while step < int(l) and flag:
        step += 1
        if compass[now_direction] == "N":
            y -= 1
        elif compass[now_direction] == "E":
            x += 1
        elif compass[now_direction] == "S":
            y += 1
        elif compass[now_direction] == "W":
            x -= 1
        
        if (0 <= x < W) and (0 <= y < H) and S[y][x] == ".":
            now_posi = (y, x)
        else:
            flag = False
            
    print(now_posi[0], now_posi[1])
    if flag == False:
        print("Stop")
        break