S = list(input())

# 小数点の削除
if "." in S: 
    i = 0
    position = S.index(".")
    S = [i for i in S if i != "."]
    S.insert(position, ".")

# 始めの余分な0を削除
if S[0] == "0":
    j = 0
    while S[j] == "0":
            j += 1
    del S[:j]

# 小数点以下の余分な0を削除
if "." in S:
    k = len(S) - 1
    while S[k] == "0":
        k -= 1
    del S[k+1:]

# 数字の始まりが小数点である場合に、頭に0を追加
if S[0] == ".":
    S.insert(0, 0)

# 数字の終わりが小数点である場合に、小数点を削除
if S[-1] == ".":
    S.remove(".")

print("".join(map(str, S)))