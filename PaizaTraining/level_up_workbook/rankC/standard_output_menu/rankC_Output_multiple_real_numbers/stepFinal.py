Q = int(input())
Ns = []
Ms = []
for i in range(Q):
    input_line = input().split(" ")
    N_i = float(input_line[0])
    M_i = int(input_line[1])
    Ns.append(N_i)
    Ms.append(M_i)

for j in range(Q):
    print("{:.{}f}".format(Ns[j], Ms[j]))