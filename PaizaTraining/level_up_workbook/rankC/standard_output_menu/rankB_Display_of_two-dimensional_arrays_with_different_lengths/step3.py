input_num = int(input())
for i in range(1, input_num+1):
    for j in range(1, i+1):
        if j == i:
            print(j)
        else:
            print(j, end=" ")