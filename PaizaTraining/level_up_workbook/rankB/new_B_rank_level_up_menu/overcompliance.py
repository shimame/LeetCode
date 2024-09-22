# 文字列の前半か後半が一致する場合、一致部分をxに置き換える.
def replace_word(half, S, v, d):
    back = half
    if d == 1:
        back -= 1
    # 前半の判定
    if S[:half] == v[:half]:
        v = "x" * half + v[half:]
    # 後半の判定
    elif S[back:] == v[back:]:
        v = v[:back] + "x" * half
    return v


N = int(input())
S = input()
results = []
for _ in range(N):
    v = input()
    ans = v
    if S == v: # 完全一致する場合
        ans = "banned"
    elif len(S) == len(v):
        if len(S) % 2 == 0:
            half = len(S) // 2
            d = 0
        else:
            half = len(S) // 2 + 1
            d = 1
        ans = replace_word(half, S, v, d)
    results.append(ans)

for i in results:
    print(i)