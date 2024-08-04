n = int(input())
a = []
index = 0
for _ in range(n):
    a.append(int(input()))
k = int(input())
for i in range(n):
    if (a[i] == k) and (index == 0):
        print(i + 1)
        break