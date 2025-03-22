# 新幹線の片道の料金を表す整数 A、ホテルの一泊あたりの料金を表す整数 B、インターンシップの回数N
a, b, n = map(int, input().split())
# 行きにかかる新幹線の片道の料金
cost = a
# インターンシップの初日を表す整数 x_i と最終日を表す整数 y_i 
internship_days = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    days = internship_days[i][0] - internship_days[i-1][1]
    if a * 2 < b * days:
        cost += a * 2
    else:
        cost += b * days
# 帰りにかかる新幹線の片道の料金
cost += a

print(cost)