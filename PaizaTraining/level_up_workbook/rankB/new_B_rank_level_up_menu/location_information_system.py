n = int(input())
t, y, x = [], [], []
for _ in range(n):
    input_line = [int(x) for x in input().split()]
    t.append(input_line[0])
    y.append(input_line[1])
    x.append(input_line[2])

now_index = 0
for i in range(101):
    if now_index < n and i == t[now_index]:
        print(y[now_index], x[now_index])
        now_index += 1
    else:
        if now_index == 0:
            print(y[0], x[0])
        else:
            pre_index = now_index - 1
            posi_y = (y[pre_index] + (i - t[pre_index]) * (y[now_index] - y[pre_index]) / (t[now_index] - t[pre_index]))
            posi_x = (x[pre_index] + (i - t[pre_index]) * (x[now_index] - x[pre_index]) / (t[now_index] - t[pre_index]))
            print(int(posi_y), int(posi_x))