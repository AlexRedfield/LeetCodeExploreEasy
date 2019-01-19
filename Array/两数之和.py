def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    _dict={}
    result=[]
    for i,num in enumerate(nums):
        if nums[i] in _dict.keys():
            result.append(i)
            result.append(_dict[nums[i]])
        else:
            _dict[target-num]=i
    return result

nums=[0,1,2]
target=3
print(two_sum(nums, target))


