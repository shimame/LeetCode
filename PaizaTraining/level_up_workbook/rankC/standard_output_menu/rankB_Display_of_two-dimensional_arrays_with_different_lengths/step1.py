input_num = int(input())
end_num = int(input_num / 2)
for i in range(2):
    start_num = i * end_num
    for j in range(1, end_num+1):
        if j == end_num or j == input_num:
            print(j+start_num)
        else:
            print(j+start_num, end=" ")