"""
for i in range(1, 6):
    for j in range(1, 5):
        print(f"{j},{i}", end=" ")
    print()

"""


count = 0
total = 0
for i in range(1, 3):
    for j in range(1, 4):
        count = count+1
        total = total + i*j
        print(count)
        