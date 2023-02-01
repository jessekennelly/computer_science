def functionA(n:int = 15):
    n = functionB()
    print("IN A ")
    return n + 1 

def functionB(n:int = 10):
    n = functionC(2*n)
    print("IN B")
    return n + 2 

def functionC(n:int):
    print("IN C ")
    return n + 5

result = functionA(3)
print(result)