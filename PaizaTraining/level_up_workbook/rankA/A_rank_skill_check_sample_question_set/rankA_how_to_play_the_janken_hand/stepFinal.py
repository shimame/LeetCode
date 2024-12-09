# N回数、M本数
N, M = [int(x) for x in input().split()]
s = list(input())

# 相手の出した手のカウント
e_g = s.count("G")
e_c = s.count("C")
e_p = s.count("P")

win_count = 0
# パーの勝ち数を上げていく(M = 2*c + 5*p であるためpの値を変更していく)
for w_p in range(M // 5 + 1):
    w_c = (M - 5 * w_p) // 2 # チョキの勝ち数
    w_g = N - (w_c + w_p) # グーの勝ち数

    if w_g < 0: # グーの勝ち数が負の時、次のw_pにうつる
        continue
    if (w_c * 2 + w_p * 5) != M: # チョキとパーに使う指の数がMと一致しないとき、次のw_pにうつる
        continue

    # 勝ちうる数と相手の手数との最小値が取りうる勝ちの最大数 min(w_g, e_c) + min(w_c, e_p) + min(w_p, e_g)
    win_count = max(win_count, min(w_g, e_c) + min(w_c, e_p) + min(w_p, e_g))

print(win_count)