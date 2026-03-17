def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    pos = len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result



set_of_nums = [
    [-4,-1,0,3,10],
    [-7,-3,2,3,11]
]


for nums in set_of_nums:
    print(f'{sortedSquares(nums)}\n')