import random
random.seed(112023)
h = int(random.random()*15)
w = int(random.random()*20)
random_numbers = [[int(random.random()*1000) for col in range(w)] for row in range(h)]

row_index = 0
for elem in random_numbers[row_index]:
    row_index += 1
print(row_index)

col_index = 0
for row in random_numbers:
    elem = row[col_index]
    col_index += 1
print(col_index)

total = 0
count = 0 
rowSum = []
for row in random_numbers:
    total2 = 0
    for elem in row:
        total += elem
        count+= 1
        total2 += elem
    rowSum.append(total2)
print(total)
print(total/count)
print(rowSum)

colSum = []
col_index2 = 0
total4 = 0
total3 = 0
for col in range(len(random_numbers[col_index])):
    total3 = 0
    for row in random_numbers:
        elem = row[col_index2]
        total3 += elem
        total4 += elem
    colSum.append(total3)
    col_index2 += 1 
    
print(total)
print(colSum)