N = int(input())
count = 0
for i in range(1, N+1):
    while i % 2 == 0:
        count += 1
        i /= 2
print(count)