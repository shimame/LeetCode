n = int(input())
x = [int(input()) for _ in range(n)]
count = 0
for i in range(1, n+1):
    if i not in x:
        count += 1
print(count)