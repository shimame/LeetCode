t, b, u, d, l, r = [int(x) for x in input().split()]
opposite_sides = {t:b, b:t, u:d, d:u, l:r, r:l}
n = int(input())
p = [int(input()) for _ in range(n)]

count = 0
now_side = p[0]
for i in range(1, n):
    if p[i] == now_side: # 次の面が同じ場合
        continue
    elif p[i] == opposite_sides[now_side]: # 次の面が裏にある場合
        count += 2
    else:
        count += 1

    now_side = p[i]
print(count)