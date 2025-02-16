n, m = map(int, input().split())
robot_operations = [list(input().split()) for _ in range(m)]
for i in range(1, n+1):
    sentence = []
    for time, operation in robot_operations:
        if i % int(time) == 0:
            sentence.append(operation)
    
    if len(sentence) == 0:
        print(i)
    else:
        print(" ".join(sentence))