N = int(input())
M = input().split(" ")
for i in range(N):
    for j in range(1, int(M[i])+1):
        if j == int(M[i]):
            print(j)
        else:
            print(j, end=" ")