'''给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
同时保持非零元素的相对顺序。'''


def move_zeroes_1(nums):
    times = 0
    for i in range(len(nums)):
        if not nums[i]:
            times += 1
    for i in range(times):
        nums.remove(0)
        nums.append(0)
    print(nums)


def move_zeroes_2(nums):
    for i in range(len(nums) - 1, -1, -1):
        if not nums[i]:
            del nums[i]
            nums.append(0)
    print(nums)


nums = [0, 1, 0, 2]
move_zeroes_2(nums)
