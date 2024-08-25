import math
A = [int(input()) for _ in range(10000)]
ans = []
x = int(math.sqrt(10000))
for i in range(0, len(A), x):
    ans.append(max(A[i:i+x]))
for j in ans:
    print(j)