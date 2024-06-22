input_line = input().split(" ")
N = int(input_line[0])
M = int(input_line[1])
A = []

for i in range(N):
    A_i = input()
    A.append(A_i)

for j in range(N):
    print("{: >{}}".format(A[j], M))