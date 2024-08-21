N, K = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
for i in range(K):
    func = input()
    if func == "pop":
        A.pop(0)
    elif func == "show":
        for j in A:
            print(j)