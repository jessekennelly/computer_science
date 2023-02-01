def transpose(l: list, l2: list):
    col_index = 0
    for i in range(len(l[0])):
        row = []
        for elem in l:
            row.append(elem[i])
        l2.append(row)
    return l2

print(transpose([[1, 2, 3, 4], [5, 6, 7, 8]], []))