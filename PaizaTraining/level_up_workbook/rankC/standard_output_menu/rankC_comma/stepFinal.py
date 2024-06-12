input_line = input()
answer_num = []
pre_position = len(input_line)
remainder = len(input_line) % 3
for i in range(len(input_line)-1, -1, -1):
    if (i-remainder) % 3 == 0:
        answer_num.append(input_line[i:pre_position])
        pre_position = i
    if i == 0 and remainder != 0:
        answer_num.append(input_line[i:pre_position])
answer_num.reverse()
print(",".join(answer_num))