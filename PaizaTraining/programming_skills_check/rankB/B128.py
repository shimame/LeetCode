n = list(map(int, list(input())))
blocks = [
    ["...", "...", "..."],  # 0
    ["#..", "...", "..."],  # 1
    ["##.", "...", "..."],  # 2
    ["###", "...", "..."],  # 3
    ["###", "#..", "..."],  # 4
    ["###", "##.", "..."],  # 5
    ["###", "###", "..."],  # 6
    ["###", "###", "#.."],  # 7
    ["###", "###", "##."],  # 8
    ["###", "###", "###"],  # 9
]

barcodes = []

# バーコードの連結
for i in range(0, len(n), 3):
    for row in range(3):
        now_row = blocks[n[i]][row] + blocks[n[i+1]][row] + blocks[n[i+2]][row]
        barcodes.append(now_row)


print("\n".join(barcodes))