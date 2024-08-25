import math

K = int(input())
A = [int(input()) for _ in range(10000)]
ans = []
x = int(math.sqrt(10000))
for _ in range(K):
    left, right = map(int, input().split())
    ans.append(max(A[left:right]))
for i in ans:
    print(i)