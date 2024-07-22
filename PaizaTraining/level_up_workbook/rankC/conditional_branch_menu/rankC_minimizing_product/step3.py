N = int(input())
A = input().split()
B = input().split()
count = 0
for i in range(N):
    if A[i] == B[i]:
        count += 1
print(count)