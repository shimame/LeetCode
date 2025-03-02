height, width = map(int, input().split())
thunder_map = [[int(x) for x in input().split()] for _ in range(height)]
risk_map = [[0] * (width//3) for _ in range(height//3)]

for h in range(0, height, 3):
    for w in range(0, width, 3):
        row0 = sum(thunder_map[h][w:w+3])
        row1 = sum(thunder_map[h+1][w:w+3])
        row2 = sum(thunder_map[h+2][w:w+3])
        ave = (row0 + row1 + row2) // 9
        risk_map[h//3][w//3] = ave

for i in range(height//3):
    print(" ".join(map(str, risk_map[i])))