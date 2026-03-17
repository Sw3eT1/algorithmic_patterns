def removeElement(nums, val):
    left = 0
    right = len(nums)

    while left < right:
        if nums[left] == val:
            nums[left] = nums[right - 1]
            nums[right - 1] = '_'
            right -= 1
        else:
            left += 1

    return nums, right



set_of_nums_and_val = {
    1:([3,2,2,3], 3),
    2:([0,1,2,2,3,0,4,2], 2)
}

for k, (nums, val) in set_of_nums_and_val.items():
    nums_final , proper_values = removeElement(nums , val)
    print(f'----------------------------------\n')
    print(f'Final version of nums: {nums_final}')
    print(f'Number of values that does not equal val: {proper_values}\n')
    print(f'----------------------------------')
