m = int(input())
n = int(input())
fax = [list(map(int, input().split())) for _ in range(n)]
amount = fax[0][2]
count = 0
for i in range(1, n):
    if fax[i][0] > fax[i-1][0]:
        count += amount // m
        if amount % m != 0:
            count += 1
        amount = fax[i][2]
    else:
        amount += fax[i][2]

count += amount // m
if amount % m != 0:
    count += 1

print(count)