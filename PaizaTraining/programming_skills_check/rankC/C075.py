balance, m = [int(x) for x in input().split()]
point = 0
for _ in range(m):
    f = int(input())
    if f < point:
        point -= f
    else:
        balance -= f
        point += f // 10
    print(balance, point)