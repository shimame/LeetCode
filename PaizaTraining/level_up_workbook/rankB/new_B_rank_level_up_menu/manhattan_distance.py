import math
P_x, P_y = [int(x) for x in input().split()]
N = int(input())
euclidean_distance = []
manhattan_distance = []
for i in range(1, N+1):
    x, y = [int(n) for n in input().split()]
    distance1 = math.sqrt((P_x - x) ** 2 + (P_y - y) ** 2)  # ユークリッド
    distance2 = abs(P_x - x) + abs(P_y - y)  # マンハッタン
    euclidean_distance.append((distance1, i))
    manhattan_distance.append((distance2, i))
euclidean_distance.sort()
manhattan_distance.sort()

for i in euclidean_distance[:3]:
    print(i[1])
for j in manhattan_distance[:3]:
    print(j[1])