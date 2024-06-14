input_nums = input().split(" ")
for i in range(len(input_nums)):
    for j in range(1, int(input_nums[i])+1):
        if j == int(input_nums[i]):
            print(j)
        else:
            print(j, end=" ")