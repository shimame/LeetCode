import math

m, n = map(int, input().split())
count = 0
for a in range(1, m):
    for b in range(1, n):
        if math.sqrt(a**2 + b**2) == int(math.sqrt(a**2 + b**2)):
            count += 1
print(count)