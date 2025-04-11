n, y = map(int, input().split())
m = int(input())
ope_log = list(map(int, input().split()))
error_count = 0
button_num = 1
f_flag = False

for i in range(m):
    if button_num != ope_log[i]:
        error_count += 1
    if error_count == y:
        f_flag = True
        break

    if button_num == n:
        button_num = 1
    else:
        button_num += 1

if f_flag:
    print(-1)
else:
    print((m - error_count) * 1000)