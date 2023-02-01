#print("Welcome to Intro to Programming")
#print(6 * (7-3) + 3 * 2**5)

def largerThan(x: int, y: int) :
    answer = False
    if x > y :
        answer = True
    else :
        answer = False
    return answer

for b in range(1,3) :
    for k in range(0,4) :
        print(f'Is {b} larger than {k}? {largerThan(b,k)}')