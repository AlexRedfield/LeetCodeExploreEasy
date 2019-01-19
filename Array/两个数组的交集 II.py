# 给定两个数组，编写一个函数来计算它们的交集。
from collections import Counter

'''
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
Counter类和其他语言的bags或multisets很相似。
'''

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # c & d 交集：min(c[x],d[x])

    # elements()返回一个迭代器，元素被重复多少次，在该迭代器中就包含多少个该元素。
    # 元素排列无确定顺序，个数小于1的元素不被包含
    return list((Counter(nums1) & Counter(nums2)).elements())


nums1 = [1, 2, 3, 1]
nums2 = [1, 1]
print(intersect(nums1, nums2))




c = Counter(a=3, b=1)
sum(c.values())  # 所有计数的总数
c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
c.items()  # 转为(elem, cnt)格式的列表
#Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
#c.most_common()[:-n:-1]  # 取出计数最少的n-1个元素
c += Counter()  # 移除0和负值
