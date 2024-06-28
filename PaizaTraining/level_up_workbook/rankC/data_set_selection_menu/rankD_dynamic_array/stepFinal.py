N, Q = map(int, input().split())
A = input().split()
for i in range(Q):
    query_i = input().split()
    if query_i[0] == "0":
        A.append(query_i[1])
    elif query_i[0] == "1":
        A.pop()
    elif query_i[0] == "2":
        print(" ".join(A))