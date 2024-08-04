N, M, K = map(int, input().split())
for _ in range(N):
    count = 0
    a = [int(x) for x in input().split()]
    for i in a:
        if i == K:
            count += 1
    print(count)