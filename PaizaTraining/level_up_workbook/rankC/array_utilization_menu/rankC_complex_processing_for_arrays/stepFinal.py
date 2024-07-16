N, Q = map(int, input().split())
queue = [int(x) + 1 for x in range(N)]
for _ in range(Q):
    S_i = input().split()
    if S_i[0] == "swap":
        A = int(S_i[1]) - 1
        B = int(S_i[2]) - 1
        tmp = queue[A]
        queue[A] = queue[B]
        queue[B] = tmp
    elif S_i[0] == "reverse":
        queue.reverse()
    elif S_i[0] == "resize":
        C = int(S_i[1])
        if C < len(queue):
            del queue[C:]

for i in queue:
    print(i)