class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                ans = mid
                left = mid + 1
        return ans

x = 8
instance = Solution()
print(instance.mySqrt(x))