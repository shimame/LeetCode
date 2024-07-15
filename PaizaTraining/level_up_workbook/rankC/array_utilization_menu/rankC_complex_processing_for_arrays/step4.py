N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
min = 200 - 100 + 1
min_pair0 = ""
min_pair1 = ""

for i in range(N - 1):
    difference = A[i + 1] - A[i]
    if min > difference:
        min = difference
        min_pair0 = A[i]
        min_pair1 = A[i + 1]

print(min_pair0)
print(min_pair1)