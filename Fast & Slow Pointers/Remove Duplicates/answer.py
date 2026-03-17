def removeDuplicates(nums):
    if not nums:
        return 0

    slow_pointer = 0

    for fast_pointer in range(1, len(nums)):
        if nums[fast_pointer] != nums[slow_pointer]:
            slow_pointer += 1
            nums[slow_pointer] = nums[fast_pointer]

    return slow_pointer + 1

set_of_nums = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4],
]

for num in set_of_nums:
    print(removeDuplicates(num))