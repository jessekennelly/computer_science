from operator import truediv


def change_of_sign(l: list):
    if l[0] > 0:
        first_element = True
    else:
        first_element = False
    
    for element in l:
        if (element > 0) == first_element:
            pass
        else:
            return True
    return False

def change_of_signn(l:list):
    for i in range(len(l) -1):
        if (l[i] > 0 and  l[i+1] < 0) or (l[i] < 0 and l[i+1] > 0):
            return True
    return False

    
assert change_of_sign([5, -1, 9, 4, -1, -2, 8]) == True, "Error: there is change of sign"
assert change_of_sign([-5, -1, -9, -4, -1, -2, -8]) == False, "Error: there is change of sign"
assert change_of_sign([5, 1, 9, 4, 1, 2, 8]) == False, "Error: there is change of sign"
print("All tests passed!")

assert change_of_signn([5, -1, 9, 4, -1, -2, 8]) == True, "Error: there is change of sign"
assert change_of_signn([-5, -1, -9, -4, -1, -2, -8]) == False, "Error: there is change of sign"
assert change_of_signn([5, 1, 9, 4, 1, 2, 8]) == False, "Error: there is change of sign"
print("All tests passed!")