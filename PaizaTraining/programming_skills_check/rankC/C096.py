n = int(input())
holidays = []

for _ in range(n):
    start, end = map(int, input().split())
    len_days = end - start
    holidays.append([start, end, len_days])

check_start, check_end, check_range = min(holidays, key=lambda x : x[2])
can_go_days = [0] * (check_range+1)

for i in range(n):
    i_person_days = [int(d) for d in range(holidays[i][0], holidays[i][1]+1)]
    for day in range(check_start, check_end + 1):
        if day in i_person_days:
            can_go_days[day-check_start] += 1

if n in can_go_days:
    print("OK")
else:
    print("NG")

"""smart_answer
n = int(input())
holidays = [list(map(int, input().split())) for _ in range(n)]
max_start_day = max(s for s, e in holidays)
min_end_day = min(e for s, e in holidays)
if max_start_day <= min_end_day:
    print("OK")
else:
    print("NG")
"""