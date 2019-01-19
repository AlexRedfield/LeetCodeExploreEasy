# matrix = [list(filter(lambda x:x!='.', i)) for i in board]

i = [1, 2, [1], 'abc']
j=[5,7]
i[:]=j
i.append(5)
print(i, j)
