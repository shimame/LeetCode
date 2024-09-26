# 整数値判定
def isint(s):
    try:
        int(s, 10)
    except ValueError:
        return False
    else:
        return True

S = input() + "x"
num_positions = []
for i in range(len(S)):
    if isint(S[i]):
        num_positions.append(i) #整数である位置を配列に追加

for j in range(len(num_positions)):
    for k in range(j, len(num_positions)):
        print(S[num_positions[j]:num_positions[k]+1])