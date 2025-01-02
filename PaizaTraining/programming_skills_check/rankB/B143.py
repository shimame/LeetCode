n, m = [int(x) for x in input().split()]
queues = [[a] for a in range(n)]

for _ in range(m):
    # 出席番号 x_i の園児が出席番号 y_i の園児に勝った
    x, y = [int(n) - 1 for n in input().split()]
    queues[x] += queues[y]

lens = list(map(len, queues))
lens_max = max(lens)
counts = lens.count(lens_max)

if counts == 1:
    print(lens.index(lens_max) + 1)
else:
    print("\n".join(map(str, [i+1 for i, x in enumerate(lens) if x == lens_max])))