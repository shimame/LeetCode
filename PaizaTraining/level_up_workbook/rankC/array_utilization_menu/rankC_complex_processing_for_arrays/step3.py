N = int(input())
A = []
for _ in range(N):
    S_i = input().split()
    if S_i[0] == "in":
        A.append(int(S_i[1]))
    elif (S_i[0] == "out") & (len(A) > 0):
        del A[0]

for i in A:
    print(i)