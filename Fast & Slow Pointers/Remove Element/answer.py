def removeElement(nums, val):

    slow_pointer = 0

    for fast_pointer in range(len(nums)):
        if nums[fast_pointer] != val:
            nums[slow_pointer] = nums[fast_pointer]
            slow_pointer += 1

    return nums, slow_pointer


set_of_nums_and_val = {
    ([3,2,2,3], 3),
    ([0,1,2,2,3,0,4,2], 2)
}

for k, (nums, val) in set_of_nums_and_val.items():
    nums_final , proper_values = removeElement(nums , val)
    print(f'----------------------------------\n')
    print(f'Final version of nums: {nums_final}')
    print(f'Number of values that does not equal val: {proper_values}\n')
    print(f'----------------------------------')
