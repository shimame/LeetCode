m, n, l = map(int, input().split())
weights = [int(input()) for _ in range(m)]
count = 0
life = l
i = 0
while i < m and n > 0:
    life -= weights[i]
    if life <= 0:
        n -= 1
        life = l
    else:
        i += 1
        count += 1
print(count)