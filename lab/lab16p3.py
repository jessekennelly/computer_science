def positive_negative_tuple(l: list):
    for element in l:
        #each time loop runs, element becomes next tuple
        if element[0] == element[1] *-1:
            return(element)
    return None




assert positive_negative_tuple([(3, 4), (5, 1), (9, -9), (7, 8)])==(9, -9), "Error: (-9, 9) is in the list"
assert positive_negative_tuple([(3, 4), (5, 1), (-3, 3), (7, 8)])==(-3, 3), "Error: (-3, 3) is in the list"
assert positive_negative_tuple([(3, 4), (5, 1), (0, 0), (7, 8)])==(0,0), "Error: should have returned (0, 0)"
assert positive_negative_tuple([(3, 4), (5, 1), (9, 9), (7, 8)])==None, "Error: no positive and negative in the list"
print("all tests passed")