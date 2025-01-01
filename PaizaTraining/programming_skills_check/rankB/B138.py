h, w = [int(x) for x in input().split()]
s = [list(input()) for _ in range(h)]
around = [(-1,-1), (-1,0), (-1,1),
          (0,-1),          (0, 1),
          (1, -1), (1, 0), (1, 1)]
donut_count = 0

for row in range(1, h-1):
    for col in range(1, w-1):
        if s[row][col] == ".":
            flag = True
            for i, j in around:
                if s[row+i][col+j] != "#":
                    flag = False
                    break
            if flag:
                donut_count += 1

print(donut_count)