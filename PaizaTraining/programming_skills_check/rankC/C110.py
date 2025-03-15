n = int(input())
days = [int(input()) for _ in range(n)]
count = 0
max_days = 0
s_day = days[0]
ans = [s_day, s_day]

for i in range(1, n):
    if days[i] - days[i-1] == 1:
        count += 1
    else:
        if max_days < count:
            ans[0] = s_day
            ans[1] = days[i-1]
            max_days = count
        s_day = days[i]
        count = 0
print(" ".join(map(str, ans)))