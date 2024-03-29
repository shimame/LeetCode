class Solution(object):
    def isValid(self, s):
        pair = {'(':')', '{':'}','[':']'}
        stack = []

        if (s[0] not in pair) or (s[-1] in pair):
            return False
        
        for i in s:
            if i in pair:
                stack.append(i)
            elif len(stack) == 0 or pair[stack.pop()] != i:
                return False
        return len(stack) == 0

s = "([]"
instance = Solution()
print(instance.isValid(s))