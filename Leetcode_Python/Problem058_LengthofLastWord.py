class Solution(object):
    def lengthOfLastWord(self, s):
        answer = []
        strs =  s.split(' ')
        for i in strs:
            if i != '':
                answer.append(i)
        return len(answer[-1])

s = "Hello World"
instance = Solution()
print(instance.lengthOfLastWord(s))