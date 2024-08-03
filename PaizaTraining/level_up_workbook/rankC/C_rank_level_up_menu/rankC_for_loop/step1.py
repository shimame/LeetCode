n = int(input())
a = [int(x) for x in input().split()]
count = 0
for i in a:
    if i % 3 == 0:
        count += 1
print(count)