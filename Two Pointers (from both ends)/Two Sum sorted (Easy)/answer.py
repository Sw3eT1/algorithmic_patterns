def twoSum(nums, target):
    if len(nums) == 2:
        return [0, 1]

    elif len(nums) < 2:
        return [-1, -1]

    else:
        left = 0
        right  = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]



set_of_nums_and_targets = {
    1:([2,3,4],6),
    2:([2, 7, 11, 15],9),
    3:([1, 3, 4, 6, 8, 11],10)
}

for k,(nums, target) in set_of_nums_and_targets.items():
    print(twoSum(nums, target))
