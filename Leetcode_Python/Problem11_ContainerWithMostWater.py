def maxArea(height):

    left = 0
    right = len(height) - 1
    width = len(height) - 1
    area = 0
    for w in range(width, 0, -1):
        if height[left] < height[right]:
            area = max(area, height[left] * w)
            left = left + 1
        else:
            area = max(area, height[right] * w)
            right = right - 1
    return area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))