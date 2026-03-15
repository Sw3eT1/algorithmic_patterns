def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0  # slow pointer

    for j in range(1, len(nums)):  # fast pointer
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

set_of_nums = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4],
]

for num in set_of_nums:
    print(removeDuplicates(num))