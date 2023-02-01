"""
def is_even(x:int):
    if x % 2 == 0:
        return True
    else: 
        return False

assert is_even(0)==True, "0 is even"
assert is_even(12)==True, "12 is even"
assert is_even(23)==False, "23 is odd"
assert is_even(-3)==False, "-3 is odd"
print("All tests passed!")
"""

def max_of_three(x: int, y: int, z: int):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return x

assert max_of_three(5, 20, 8) == 20, "20 should be the maximum"       
assert max_of_three(15, 4, 8) == 15, "15 should be the maximum"       
assert max_of_three(5, 20, 80) == 80, "80 should be the maximum"       
assert max_of_three(18, 1, 18) == 18, "18 should be the maximum"
assert max_of_three(1, 1, 18) == 18, "18 should be the maximum"
assert max_of_three(-18, -18, -18) == -18, "-18 should be the maximum"
print("All tests passed!")
