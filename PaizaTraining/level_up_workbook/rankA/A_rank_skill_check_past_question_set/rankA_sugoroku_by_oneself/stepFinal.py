t, b, u, d, l, r = [int(x) for x in input().split()]
opposite_sides = {t:b, b:t, u:d, d:u, l:r, r:l}

n = int(input())
p = [int(input()) for _ in range(n)]

current_side = t
count = 0
for i in range(1, n):
    if p[i] == current_side:
        continue
    elif p[i] == opposite_sides[current_side]:
        current_side = p[i]
        count += 2
    else:
        current_side = p[i]
        count += 1

print(count)