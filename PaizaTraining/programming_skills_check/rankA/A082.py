h, w = map(int, input().split())
king_map = [list(input()) for _ in range(h)]
around_lake_maps = [[0] * w for _ in range(h)]
const_count = 0

def counting_lake(r, c):
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for dy, dx in dire:
        y, x = r + dy, c + dx
        if 0 <= y <= h-1 and 0 <= x <= w-1 and king_map[y][x] == "#":
            count += 1
    return count

for row in range(h):
    for col in range(w):
        if king_map[row][col] == "#":
            aro_count = counting_lake(row, col)
            around_lake_maps[row][col] = aro_count
        else:
            const_count += 1

for r in range(h):
    for c in range(w):
        if king_map[r][c] == "#":
            king_map[r][c] = "."
            lake_count = counting_lake(r, c)
            if around_lake_maps[r][c] == lake_count:
                const_count += 1
            king_map[r][c] = "#"

print(const_count)