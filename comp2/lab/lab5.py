from time import time
n = 100
nested_list = [[j * n + i+1 for i in range(n)] for j in range(n)]
def max(some_list: list)-> int:
    max = some_list[0][0]
    for row in some_list:
        for value in row:
            if value > max:
                max = value
    return max

def normalize(some_list: list)->list:
    scaled = [[value/max(some_list) for value in row] for row in some_list]
    return scaled

#main


#Time the following function call
start = time()
scaled = normalize(nested_list)
end = time()
print(end-start)