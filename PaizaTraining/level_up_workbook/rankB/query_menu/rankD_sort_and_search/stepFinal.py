N, K, P = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
A.append(P)
for _ in range(K):
    input_line = input().split()
    event = input_line[0]
    if event == "join":
        num = int(input_line[1])
        A.append(num)
    elif event == "sorting":
        print(sorted(A).index(P) + 1)