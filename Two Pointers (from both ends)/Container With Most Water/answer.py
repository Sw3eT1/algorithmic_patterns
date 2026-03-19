def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area



set_of_nums = [
    [1,8,6,2,5,4,8,3,7],
    [1,1],
    [1,2],
    [1,2,4,3],
    [4,3,2,1,4]
]

for nums in set_of_nums:
    print(maxArea(nums))