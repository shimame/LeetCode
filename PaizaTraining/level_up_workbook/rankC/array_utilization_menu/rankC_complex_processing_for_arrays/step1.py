N = int(input())
M = list(map(int, input().split()))
scores = []
for _ in range(N):
    A = list(map(int, input().split()))
    AM_sum = sum([a * m for (a, m) in zip(A, M)])
    scores.append(AM_sum)

print(max(scores))