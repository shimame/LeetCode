n = int(input())
weights = [int(input()) for _ in range(n)]

max_diet_days = 0
max_cheat_days = 0 
now_diet_days = 0
now_cheat_days = 0

for i in range(1, n):
    if weights[i-1] > weights[i]:  # 痩せ
        now_diet_days += 1
        max_diet_days = max(max_diet_days, now_diet_days)
        now_cheat_days = 0
    else: # 太る
        now_cheat_days += 1
        max_cheat_days = max(max_cheat_days, now_cheat_days)
        now_diet_days = 0

print(max_diet_days, max_cheat_days)