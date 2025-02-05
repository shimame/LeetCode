n = int(input())
balls = [int(input()) for _ in range(n)]
m = int(input())
for _ in range(m):
    a, b, x = [int(i) for i in input().split()]
    if balls[a-1] < x:
        balls[b-1] += balls[a-1]
        balls[a-1] = 0
    else:
        balls[a-1] -= x
        balls[b-1] += x
print("\n".join(map(str, balls)))