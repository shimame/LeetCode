input_line = input()
answer_num = []
pre_position = 0
for i in range(len(input_line)):
    if (i+1) % 3 == 0:
        answer_num.append(input_line[pre_position:i+1])
        pre_position = i+1
print(",".join(answer_num))