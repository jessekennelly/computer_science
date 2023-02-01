nested_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

#iterates over single row
row_index = 1
for elem in nested_list[row_index]:
    print(elem)

#iterates over single col
col_index = 1
for row in nested_list:
    elem = row[col_index]
    print(elem)

#iterates over every element by row
total = 0
for row in nested_list:
    for elem in row:
        #total += elem
        print(elem)
    #print(total)

#iterates over every element by column
col_index2 = 0
for col in range(len(nested_list[0])):
    for row in nested_list:
        elem = row[col_index2]
        print(elem)