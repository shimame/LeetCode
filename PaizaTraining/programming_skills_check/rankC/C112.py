n = int(input())
min_time = 100
max_time = 0
for _ in range(n):
    s, f, t = [int(x) for x in input().split()]
    day_time = s + f + 24 - t
    if day_time < min_time:
        min_time = day_time
    if day_time > max_time:
        max_time = day_time
print(min_time)
print(max_time)