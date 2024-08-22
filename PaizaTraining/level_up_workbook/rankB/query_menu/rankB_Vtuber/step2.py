N, K = map(int, input().split())
members = [input() for _ in range(N)]
reporters = []
for i in range(K):
    reporter = input().split()
    reporter[0] = int(reporter[0])
    reporters.append(reporter)
for i in sorted(reporters, key = lambda x: x[0]):
    print(i[1])