def has_zeroes(l: list):
    for i in range(len(l)):
        if l[i] == 0:
            return True
    else:
        return False

assert has_zeroes([0,1,2])==True, "Error: the list [0, 1, 2] does have a 0"
assert has_zeroes([1,2,3])==False, "Error: the list [1, 2, 3] does not have a 0"
assert has_zeroes([2,1,0])==True, "Error: the list [2, 1, 0] does have a 0"
assert has_zeroes([0]) == True, "Error: the list [0] does have a 0"
assert has_zeroes([]) == False, "Error: the list [] does not have a 0"
print("All tests passed!")