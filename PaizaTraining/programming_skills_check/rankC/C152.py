d = int(input())
# 0が晴れ、 1がくもり、 2が雨
weathers = list(map(int, input().split()))
rainbow_days = []

# 虹が出る可能性のある日とは、前日が雨の日である晴れの日 2->0
for day in range(d-1):
   if weathers[day] == 2 and weathers[day+1] == 0:
    rainbow_days.append(day+1)

if len(rainbow_days) == 0:
    print(-1)
else:
    print(" ".join(map(str, rainbow_days)))