nums = [2,7,11,15]
target = 9
answer = 0
for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        answer = num1 + num2
        if(target == answer and i < j):
            print(str(i) + "," + str(j))
            
            '''
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            '''
        