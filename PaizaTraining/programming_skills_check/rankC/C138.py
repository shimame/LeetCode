n = int(input())
records = [int(input()) for _ in range(n)]
sorted_rec = sorted(records, reverse=True)
rec_ranks = {}
rank = 1

for i in range(n):
    if sorted_rec[i] not in rec_ranks:
        rec_ranks[sorted_rec[i]] = rank
    rank += 1

for j in range(n):
    print(rec_ranks[records[j]])