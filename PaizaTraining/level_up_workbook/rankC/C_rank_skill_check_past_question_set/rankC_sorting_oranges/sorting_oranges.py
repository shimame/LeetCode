N, M = map(int, input().split())
results = []
for _ in range(M):
    orange_gram = int(input())
    if orange_gram < N * 1.5:
        result = N
    elif orange_gram % N < N / 2:
        result = (orange_gram // N) * N
    else:
        result = (orange_gram // N + 1) * N
    results.append(result)

for i in results:
    print(i)