H, W, D = [int(x) for x in input().split()]
nums = [int(x) for x in range(1, H*W+1)]
l_map = [[0 for _ in range(W)] for _ in range(H)]
# 右上
if D == 1:
    row, col = 0, 0
    while row >= 0 and col < W:
        row -= 1
# 右
elif D == 2:
    for i in range(H):
        l_map[i] = nums[i:i+W]

# 下
elif D == 3:
    H, W = W, H
    for i in range(H):
        l_map[i] = nums[i:i+W]
    l_map = zip(*l_map)

# 左下
elif D == 4:
    row, col = 0, 0
    while row 