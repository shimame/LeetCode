x, y, z = map(int, input().split())
n = int(input())
total = 0

for _ in range(n):
    start, end = map(int, input().split())
    times = [0, 0, 0]
    for i in range(start, end):
        if 9 <= i < 17:
            times[0] += 1
        elif 17 <= i < 22:
            times[1] += 1
        else:
            times[2] += 1
    total += times[0] * x + times[1] * y + times[2] * z
print(total)