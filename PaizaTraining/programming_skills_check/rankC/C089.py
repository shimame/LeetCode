h, w = [int(x) for x in input().split()]
s = [list(input()) for _ in range(h)]
total_point = 0

for i in range(h):
    points = [int(y) for y in input().split()]
    for col in range(w):
        if s[i][col] == "o":
            total_point += points[col]

print(total_point)