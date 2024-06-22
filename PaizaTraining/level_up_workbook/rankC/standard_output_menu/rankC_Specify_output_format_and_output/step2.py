input_line = input().split(" ")
N = int(input_line[0])
A = int(input_line[1])
B = int(input_line[2])

answer = []
for i in range(N):
    answer.append(("({}, {})".format(A, B)))

print(", ".join(answer))