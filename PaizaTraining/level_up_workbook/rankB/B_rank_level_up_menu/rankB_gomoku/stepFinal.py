# 右上
def determination_five_upper_right(S, N):
    result = ""
    row, col = N - 1, 0
    l = ""
    while row >= 0 and col < N:
        l += S[row][col]
        row -= 1
        col += 1
    if l == "O" * N:
        result = "O"
    elif l == "X" * N:
        result = "X"
    return result

# 一行ずつ
def determination_five_row(S, N):
    result = ""
    i = 0
    while i < N and result == "":
        if "".join(S[i]) == "O" * N:
            result = "O"
        elif "".join(S[i]) == "X" * N:
            result = "X"
        i += 1
    return result

s = [input() for _ in range(5)]
N = 5
results = []

# 横
results.append(determination_five_row(s, N))

# 縦
t_s = list(zip(*s))
results.append(determination_five_row(t_s, N))

# 右斜め diagonally_right
results.append(determination_five_upper_right(s, N))

# 左斜め
dl_s = []
for i in range(N):
   dl_s.append(list(reversed(s[i])))
results.append(determination_five_upper_right(dl_s, N))

if "O" in results:
    print("O")
elif "X" in results:
    print("X")
else:
    print("D")