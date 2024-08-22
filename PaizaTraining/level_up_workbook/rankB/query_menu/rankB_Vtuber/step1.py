N, K =  [int(x) for x in input().split()]
names = [input() for _ in range(N)]
for _ in range(K):
    input_line = input().split()
    event = input_line[0]
    if event == "join":
        name = input_line[1]
        names.append(name)
    elif event == "leave":
        name = input_line[1]
        names.remove(name)
    elif event == "handshake":
        for i in sorted(names):
            print(i)