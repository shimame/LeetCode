class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        num = 0
        i = 0
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num = num * sign

        if num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif num < -pow(2, 31):
            return -pow(2, 31)
        
        return num

isinstance = Solution()
s = "4193 with words"
#words and 987
print(isinstance.myAtoi(s))