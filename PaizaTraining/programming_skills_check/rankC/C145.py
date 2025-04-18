import math

n = int(input())
scores = list(map(int, input().split()))
scores.sort()
del scores[0]
del scores[-1]

ave = sum(scores) / (n-2)
print(math.floor(ave * 10) / 10)