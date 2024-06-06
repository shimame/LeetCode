input_line = input()
s = []
for i in range(len(input_line)):
    if input_line[i] == " ":
        s.append(",")
    else:
        s.append(input_line[i])
print("".join(s))