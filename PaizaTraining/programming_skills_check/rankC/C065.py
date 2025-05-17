n = int(input())
ans_nums = [i for i in range(1, 101)]

for _ in range(n):
    o, x = input().split()
    if o == ">":
        ans_nums = [i for i in ans_nums if i > int(x)]
    elif o == "<":
        ans_nums = [i for i in ans_nums if i < int(x)]
    elif o == "/":
        ans_nums = [i for i in ans_nums if i % int(x) == 0]

print(ans_nums.pop(0))