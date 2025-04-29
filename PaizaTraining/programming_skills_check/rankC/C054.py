n, v = map(int, input().split())
time_posi = [list(map(int, input().split())) for _ in range(n)]
pre_time, pre_posi = time_posi[0]
flag = True

for i in range(1, n):
    now_time, now_posi = time_posi[i]
    if (now_posi - pre_posi) / (now_time - pre_time) > v:
        print("YES")
        flag = False
        break
    pre_time, pre_posi = now_time, now_posi

if flag:
    print("NO")