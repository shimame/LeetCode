n = int(input())
total_time = 0
for _ in range(n):
    start, end = input().split()
    s_hour, s_min = start.split(":")
    e_hour, e_min = end.split(":")
    hour = int(e_hour) - int(s_hour)
    min = int(e_min) - int(s_min) + hour * 60
    total_time += min
print(total_time// 60, total_time % 60)