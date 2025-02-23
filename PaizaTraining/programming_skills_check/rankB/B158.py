n = int(input())
center = n // 2 + 1
pyramid_map = [[0] * n for _ in range(n)]
start = 0
end = n - 1
amount = 0

# ピラミッド状に正方形をつくる
for num in range(1, center+1):
    for posi in range(start, end+1):
        # 囲いたい枠の上下の行を変更
        pyramid_map[start][posi] = num
        pyramid_map[end][posi] = num
        # 囲いたい枠の左右の列を変更
        pyramid_map[posi][start] = num
        pyramid_map[posi][end] = num
    start += 1
    end -= 1

stones = [[int(x) for x in input().split()] for _ in range(n)]

for row in range(n):
    for col in range(n):
       amount += stones[row][col] - pyramid_map[row][col]

print(amount)