class Solution(object):
    def reverse(self, x):
        str_x = str(x)
        r_str_x = str_x[::-1]
        if r_str_x[-1] == "-":
            r_str_x = r_str_x.replace("-", " ")
            r_str_x = "-" + r_str_x
        if int(r_str_x) <= pow(2, 31) - 1 and int(r_str_x) >= -pow(2, 31):
            return int(r_str_x)
        else:
            return 0

isinstance = Solution()
x = -1534236469
print(isinstance.reverse(x))