N = int(input())
listeners = {}
memberships = {}
for _ in range(N):
    input_line = input().split()
    name = input_line[0]
    func = input_line[1]
    if func == "give":
        if name not in listeners:
            listeners[name] = 0
        money = int(input_line[2])
        listeners[name] += money
    elif func == "join":
        if name not in listeners:
            memberships[name] = 0
        else:
            memberships[name] = listeners[name]
for name, money in sorted(listeners.items(), key=lambda x: (x[1], x[0]), reverse=True):
    print(name)
for j in sorted(memberships):
    print(j)