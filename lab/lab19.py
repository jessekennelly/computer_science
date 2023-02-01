"""
Write a program that asks a user for a password and checks if their password is valid. 
Passwords must be at least 10 characters long, contain at least one upper-case letter, 
contain at least one number (Hint: look through the string functions), and contain at 
least one special character from ! or @.
"""



password = input("Enter your password: ")

if len(password) < 10:
    print("Invalid password. Must be longer than 10 characters.")
    password = input("Enter your password: ")

if password.islower() == True:
    print("Invalid password. Must include at least one uppercase character")
    password = input("Enter your password: ")

if password.isalpha() == True:
    print("Invalid password. Must contain at least one number")
    password = input("Enter your password: ")


if password.find("!") == -1 and password.find("@") == -1:
    print("Invalid password. Must contain at least one special character")
    password = input("Enter your password: ")
print("Valid password.")