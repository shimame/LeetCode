H, W, N = [int(x) for x in input().split()]
C = [[int(i) for i in input().split()] for _ in range(H)]
counts = []
for _ in range(N):
    count = 0
    y, x, B, S = map(int, input().split())
    y -= 1
    x -= 1
    w_B = int((B - 1) / 2)
    w_S = int((S - 1) / 2)
    for i in range(B):
        for j in range(B):
            count += C[y-w_B+i][x-w_B+j]
    for k in range(S):
        for l in range(S):
            count -= C[y-w_S+k][x-w_S+l]
    counts.append(count)
for c in counts:    
    print(c)