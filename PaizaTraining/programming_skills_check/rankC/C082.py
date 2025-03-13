x, y = map(int, input().split())
english_scores = []
japanese_scores = []
math_scores = []
student_fail_counts = [0] * x

# 英語、国語、数学のテストの点数を学籍番号と点数でタプルにして各教科ごとの配列に追加する。
for i in range(x):
    eng, jap, math = map(int, input().split())
    english_scores.append((i, eng))
    japanese_scores.append((i, jap))
    math_scores.append((i, math))

# 昇順にソート
english_scores.sort(key=lambda x:x[1])
japanese_scores.sort(key=lambda x:x[1])
math_scores.sort(key=lambda x:x[1])

# 各教科の赤点の点数
e_fail_score = english_scores[y-1][1]
j_fail_score = japanese_scores[y-1][1]
m_fail_score = math_scores[y-1][1]

e_flag, j_flag, m_flag = False, False, False

# 昇順にソートした配列を頭から順に参照する。
for j in range(x):
    # 英語の点数が赤点以下なら、その学籍番号の赤点数の値に1加える。
    if english_scores[j][1] <= e_fail_score:
        student_fail_counts[english_scores[j][0]] += 1
    else:
        e_flag = True
    
    # 国語の点数が赤点以下なら、その学籍番号の赤点数の値に1加える。
    if japanese_scores[j][1] <= j_fail_score:
        student_fail_counts[japanese_scores[j][0]] += 1
    else:
        j_flag = True
    
    # 数学の点数が赤点以下なら、その学籍番号の赤点数の値に1加える。
    if math_scores[j][1] <= m_fail_score:
        student_fail_counts[math_scores[j][0]] += 1
    else:
        m_flag = True
    
    # 全ての教科の点数が赤点より上の場合
    if e_flag and j_flag and m_flag:
        break

print("\n".join(map(str, student_fail_counts)))