N, M = [int(x) for x in input().split()]
intervals = [int(input()) for _ in range(M)]
scores = [0] * N

for i in range(N):
    score = 100
    for j in range(M):
        now_interval = int(input())
        dif = abs(intervals[j] - now_interval)
        if dif < 5:
            continue
        elif dif <= 10:
            score -= 1
        elif dif <= 20:
            score -= 2
        elif dif <= 30:
            score -= 3
        else:
            score -= 5

    if score > 0:
        scores[i] = score

print(max(scores))