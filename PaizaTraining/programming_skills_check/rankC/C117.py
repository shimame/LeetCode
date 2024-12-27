n, m = [int(x) for x in input().split()]
a, b, c = [int(y) for y in input().split()]
count = 0
for _ in range(n):
    r_i = int(input())
    result = r_i * c - a - b * m 
    if result < 0:
        count += 1
print(count)