a, b, R = [int(c) for c in input().split()]
n = int(input())
for _ in range(n):
    x, y = [int(d) for d in input().split()]
    if (x - a)**2 + (y - b)**2 >= R**2:
        print("silent")
    else:
        print("noisy")