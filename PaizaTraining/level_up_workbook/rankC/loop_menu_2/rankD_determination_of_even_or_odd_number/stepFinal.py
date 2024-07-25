N = int(input())
nums = [int(x) for x in input().split()]
for i in nums:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")