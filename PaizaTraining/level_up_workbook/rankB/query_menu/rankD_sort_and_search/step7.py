N, K = map(int, input().split())
students = {num:id for num, id in [input().split() for _ in range(N)]}
"""
for _ in range(N):
    num, id = input().split()
    students[num] = id
"""
for _ in range(K):
    input_line = input().split()
    func = input_line[0]
    num = input_line[1]
    if func == "join":
        id = input_line[2]
        students[num] = id
    elif func == "leave":
        del students[num]
    elif func == "call":
        print(students[num])