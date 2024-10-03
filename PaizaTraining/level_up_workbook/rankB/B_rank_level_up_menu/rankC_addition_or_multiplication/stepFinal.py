n = int(input())
sum = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    if a == b:
        sum += a * b
    else:
        sum += a + b
print(sum)