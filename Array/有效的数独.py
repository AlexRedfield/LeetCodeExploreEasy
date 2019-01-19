'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
'''

def is_valid_sudoku1(board):
    for i in range(9):
        if 9 - len(set(board[i])) != board[i].count(".") - 1:  # 条件一
            return False

        new_list = []
        for j in range(9):  # 条件二
            if board[j][i] != '.' and board[j][i] in new_list:
                return False
            if board[j][i] != '.' and board[j][i] not in new_list:
                new_list.append(board[j][i])

    aa, bb = [0, 3, 6], [0, 3, 6]
    for a in aa:  # 条件三
        for b in bb:
            new_list = []
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    if board[i][j] != '.' and board[i][j] in new_list:
                        return False
                    if board[i][j] != '.' and board[i][j] not in new_list:
                        new_list.append(board[i][j])

    return True


def is_valid_sudoku2(board):
    row = ['' for i in range(9)]
    col = ['' for i in range(9)]
    cell = ['' for i in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = board[i][j]
                k = i // 3 * 3 + j // 3  # k为该元素所在子区的序号
                if num in row[i] + col[j] + cell[k]:  # 将3个list顺序拼接
                    return False
                row[i] += num
                col[j] += num
                cell[k] += num

    return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(is_valid_sudoku1(board1))

'''
board2=[['1' for j in range(10000)] for i in range(100000) ]
time1=time.clock()
print(is_valid_sudoku1(board2))
print(time.clock()-time1)

time2=time.clock()
print(is_valid_sudoku2(board2))
print(time.clock()-time2)
'''
