import math
def sum_and_average(l:list) -> tuple:
    total = 0
    avg = 0
    for element in l:
        total += element
        avg = total / len(l)
    return (total, avg)

assert sum_and_average([5, -3, 1, 8])[0] == 11 and math.isclose(sum_and_average([5, -3, 1, 8])[1], 2.75), "Incorrect sum and average for list [5, -3, 1, 8]"
assert sum_and_average([5])[0] == 5 and math.isclose(sum_and_average([5])[1], 5.0),"Incorrect sum and average for one element"
print("All tests passed!")
 