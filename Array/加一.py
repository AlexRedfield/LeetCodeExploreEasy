'''
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
'''


def plus_one(digits):
    length = len(digits)
    num = 0
    total = 0
    for i in range(length):
        num += 1
        total += digits.pop() * 10 ** (num - 1)

    # 将结果字符化
    total = str(total + 1)
    print(total)
    result = []
    for i in range(len(total)):
        result.append(int(total[i]))

    print(result)
    return result


plus_one([0, 9])
