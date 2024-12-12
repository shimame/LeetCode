t, b, u, d, l, r = [int(x) for x in input().split()]
opposite_sides = {t:b, b:t, u:d, d:u, l:r, r:l}
q = int(input())
print(opposite_sides[q])