# 给定一个数组，将数组中的元素向右移动 k 个位置（k>=0）。


# 将数组的前k个元素和剩余元素倒置，再将整个数组倒置
def rotate(nums, k):
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)
    print(nums)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


rotate([1, 2, 3, 4, 5], 3)
