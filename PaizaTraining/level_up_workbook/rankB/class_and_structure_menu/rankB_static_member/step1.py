N = int(input())
roster = []
answer = []
for _ in range(N):
    input_line = input().split()
    if "make" == input_line[0]:
        roster.append(input_line)
    elif "getnum" == input_line[0]:
        answer.append(roster[int(input_line[1]) - 1][1])
    elif "getname" == input_line[0]:
        answer.append(roster[int(input_line[1]) - 1][2])
for i in answer:
    print(i)