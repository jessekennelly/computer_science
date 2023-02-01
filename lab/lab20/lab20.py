import random
f = open("lab/lab20/usa.txt", "r")
my_list = list(f)
num = int(input("How many words? "))
password = []
for i in range(num):
    password.append(random.choice(my_list))

for i in range(len(password)):
    password[i] = password[i].capitalize()
    password[i] = password[i].strip()
    print(password[i], end ="")