# 给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
# 必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


#先将对角线以上的元素转置，然后将矩阵每行倒置
def rotate1(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(length):
        # matrix[i].reverse()
        matrix[i] = matrix[i][::-1]  # 倒置之后浅拷贝


def rotate2(matrix):
    matrix[:] = map(list, zip(*matrix[::-1]))


matrix1 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
rotate2(matrix1)
print(matrix1)
