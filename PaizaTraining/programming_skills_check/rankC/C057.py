t, x, y = map(int, input().split())
max_x = x

for _ in range(t):
    a, b = map(int, input().split())
    if y > 0:
        x += a
        y += b
        if x > max_x:
            max_x = x
print(max_x)