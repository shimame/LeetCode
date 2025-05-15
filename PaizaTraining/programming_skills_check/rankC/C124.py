n = int(input())
schedule = [0] * 1001
add_flag = False
count = 0
for _ in range(n):
    num = int(input())
    for _ in range(num):
        start, term = map(int, input().split())
        if all(x == 0 for x in schedule[start:start+term]):
            add_flag = True
            for i in range(start, start+term):
                schedule[i] = 1
    if add_flag:
        count += 1
        add_flag = False
print(count)