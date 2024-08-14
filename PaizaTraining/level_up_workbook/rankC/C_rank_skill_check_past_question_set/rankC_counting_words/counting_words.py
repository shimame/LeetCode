words = [x for x in input().split()]
dic = {}
for i in words:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in dic:
    print(i, dic[i])