def calculation_sum_upper_right(A, N):
    start_position = []
    # 一番左の縦列をスタートの位置に追加する
    for i in range(N):
        start_position.append((i, 0))

    # 一番下の行をスタートの位置に追加する
    for i in range(1, N):
        start_position.append((N-1, i))

    # 一番左,下の列から右上の順に合計を計算する
    sums = []
    for row, col in start_position:
        total = 0
        while row >= 0 and col <= N - 1:
            total += A[row][col]
            row -= 1
            col += 1
        sums.append(total)
    return sums

# 一行ずつ合計を計算してする
def calculation_sum_row(A, N):
    sums = []
    for i in range(N):
        total = sum(A[i])
        sums.append(total)
    return sums

N = int(input())
A = []
all_sums = []
for _ in range(N):
    a = [int(x) for x in input().split()]
    A.append(a)
# 横
row_sum = calculation_sum_row(A, N)
all_sums += row_sum

# 縦
t_A = list(zip(*A))
col_sum = calculation_sum_row(t_A, N)
all_sums += col_sum

# 右斜め diagonally_right
dr_sum = calculation_sum_upper_right(A, N)
all_sums += dr_sum

# 左斜め
dl_A = []
for i in range(N):
    dl_A.append(list(reversed(A[i])))
dl_sum = calculation_sum_upper_right(dl_A, N)
all_sums += dl_sum

print(max(all_sums))