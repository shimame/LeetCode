n = int(input())
scores = list(map(int, input().split()))
rank = sorted(scores, reverse=True)
rank_dict = {}
count = 1

for i in rank:
    if i not in rank_dict:
        rank_dict[i] = count
    count += 1

for j in scores:
    if rank_dict[j] == 1:
        print("G")
    elif rank_dict[j] == 2:
        print("S")
    elif rank_dict[j] == 3:
        print("B")
    else:
        print("N")