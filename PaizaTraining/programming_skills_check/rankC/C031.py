n = int(input())
citys = {}

for _ in range(n):
    p, s = input().split()
    citys[p] = int(s)

q, t = input().split()
hour, minute = map(int, t.split(":"))
additonal_hour_time = hour - citys[q]

for p, s in citys.items():
    s += additonal_hour_time
    if s < 0:
        s += 24
    elif s >= 24:
        s -= 24
    print(str(s).zfill(2) + ":" + str(minute).zfill(2))