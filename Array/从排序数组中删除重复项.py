# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    number = 0  # 记录数组中不同数字的个数
    length = len(nums)

    # 数组长度为零的情况
    if not length:
        return 0

    for i in range(length):
        if nums[i] != nums[number]:
            number += 1
            nums[number] = nums[i]

    return number + 1


print(remove_duplicates([1, 2, 2, 3, 3]))
