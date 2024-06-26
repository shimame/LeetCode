input_num = list(map(int, input().split()))
input_num.sort()
print(input_num[len(input_num) - 1] - input_num[0])