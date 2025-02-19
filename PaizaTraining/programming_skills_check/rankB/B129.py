n, m = [int(x) for x in input().split()]
h, w = [int(y) for y in input().split()]
field = [["."] * w for _ in range(h)]
amounts = [0] * m
for _ in range(n):
    # h, h, w, w, m
    a, b, c, d, e = [int(z) - 1 for z in input().split()]
    amount = 0
    for row in range(a, b+1):
        for col in range(c, d+1):
            if field[row][col] != ".":
                amounts[field[row][col] - 1] += 1
            field[row][col] = e + 1

for i in amounts:
    print(i)

for j in range(h):
    print("".join(map(str, field[j])))