nums = input().split(" ")
N = int(nums[0])
M = int(nums[1])
A = input().split(" ")
B = input().split(" ")

for i in range(M):
    for j in range(int(B[i])):
        if j == int(B[i]) - 1:
            print(A[j])
        else:
            print(A[j], end=" ")
    del A[:int(B[i])]