N = int(input())
A = [x for x in input().split()]
count = 0
for i in A:
    if i == "1":
        count += 1
print(count)