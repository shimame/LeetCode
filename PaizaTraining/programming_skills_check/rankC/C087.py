num = input()
reverse_num = num[::-1]
while num != reverse_num:
    num = str(int(num) + int(reverse_num))
    reverse_num = num[::-1]
print(num)