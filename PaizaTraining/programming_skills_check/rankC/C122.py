n, x, y = map(int, input().split())
merchandises = [int(input()) for _ in range(n)]
total = sum(merchandises)
if n >= x:
    merchandises.sort()
    total -= sum(merchandises[:y])
print(total)