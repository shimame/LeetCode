from fractions import Fraction

n = int(input())
nums = list(int(input()) for _ in range(n))
cal = nums[-1]
for i in range(n-2, -1, -1):
    cal = Fraction(nums[i], 1) + Fraction(1, cal)
print(" ".join(str(cal).split("/")))