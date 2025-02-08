n, d = [int(a) for a in input().split()]
h_x, h_y = [int(b) for b in input().split()]
count = 0

for _ in range(n):
    x, y = [int(c) for c in input().split()]
    dis = abs(h_x - x) + abs(h_y - y)
    if dis <= d:
        count += 1

print(count)