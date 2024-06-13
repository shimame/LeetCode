input_num = int(input())
for i in range(1, input_num + 1):
    for j in range(1, input_num + 1):
        if j == input_num:
            print(i * j)
        else:
            print(i * j, end=" ")