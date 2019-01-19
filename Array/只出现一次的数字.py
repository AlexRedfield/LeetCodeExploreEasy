# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
# 找出那个只出现了一次的元素。
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？


def single_number1(nums):
    # 特殊情况检测
    if len(nums) < 2:
        return nums[0]

    nums.sort()

    # 将数组中元素与前后比较，都不同则返回该元素
    for i in range(1, len(nums) - 1):
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]
    # 检测首尾元素
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]


def single_number2(nums):
    return sum(set(nums)) * 2 - sum(nums)


print(single_number1([0, 4, 4, 1, 2, 1, 2]))
