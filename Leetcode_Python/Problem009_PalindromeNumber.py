class Solution(object):
    def isPalindrome(self, x):
        if(x >= 0):
            y = str(x)[::-1]
            if(x == int(y)):
                return True
            else:
                return False
        else:
            return False

x = -121
isinstance = Solution()
print(isinstance.isPalindrome(x))