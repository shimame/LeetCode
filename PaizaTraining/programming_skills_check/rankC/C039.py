e = list(input())
nums = []
ten_count = 0
one_count = 0
for i in e:
    if i == "+":
        nums.append(ten_count * 10 + one_count)
        ten_count, one_count = 0, 0
    elif i == "<":
        ten_count += 1
    else:
        one_count += 1
nums.append(ten_count * 10 + one_count)
print(sum(nums))