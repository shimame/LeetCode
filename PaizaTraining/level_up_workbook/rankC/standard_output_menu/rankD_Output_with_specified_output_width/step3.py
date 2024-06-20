N = int(input())
M = []
for i in range(N):
    M_i = input()
    M.append(M_i)

for j in range(N):
    print("{: >3}".format(M[j]))