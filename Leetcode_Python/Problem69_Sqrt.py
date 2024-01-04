def mySqrt(x):
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

x = 2147395599
print(mySqrt(x))