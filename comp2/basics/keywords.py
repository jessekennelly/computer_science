def func(a, b, c = 5):
    return a + b + c

#no value for c was given, so it uses its default, 5
print(func(1, 2))

#careful with using mutable objects as default arguments 
#def func(a, b, c=[])



#call stack
def one(a):
    print("Inside one!")
    print(a)

def two(b):
    print("Inside two!")
    print(b)

two(24)

#Call Stack that reaches line 3

#one(), line 14, a = 101
#two, line 18, b = 24
#main code block b = 24

def function1(n:int)->int: 
    print("In function1:", n) 
    n = function2(n+1) 
    print("Returned from function2, back in function1", n) 
    return n 
 
def function2(n:int)->int: 
    print("In function2:", n) 
    n = function3(n+1) 
    print("Returned from function3, back in function2", n) 
    return n+1 
 
def function3(n:int)->None: 
    print("In function3:", n) 
    return n+1 
 
def function4(n:int)->int: 
    print("In function4:", n) 
    n = function1(n+1) 
    print("Returned from function1, back in function4", n) 
    return n+1 
 
result = function1(17) 
print(result) 