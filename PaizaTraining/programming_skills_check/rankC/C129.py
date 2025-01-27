n, m = [int(x) for x in input().split()]
A = [int(input()) for _ in range(m)]
B = {}
flag = "Yes"
for _ in range(m):
    num = int(input())
    if num not in B:
        B[num] = 1
    else:
        B[num] += 1

for i in B:
    if B[i] == A.count(i):
        continue
    else:
        flag = "No"
        break
print(flag)