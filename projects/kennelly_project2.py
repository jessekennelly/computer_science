"""
Takes in user height in meters and converts to feet and leftover inches. If the height is negative then
an error message will be displayed

File Name: kennelly_project2.py
Author: Jesse Kennelly
Date: 9/19/22
Course: COMP1351
Assignment: Project 2 - Height Converter
Collaborators: none
Internet Source: none
"""

height_meter = float(input("Enter the height in meters: "))
#takes float meter and converts it to int for feet
height_feet = int(height_meter / .3048)
#mod meter gives the decimal value which is inches, then * 12 to give whole number
height_inches = height_meter /.3048 % 1 * 12

#checks to make sure the number is not negative
if height_meter > 0:
    
    print(f"A height of {height_meter} meters is {height_feet} feet and {height_inches} inches")
#if the number is negative, then the error message will output
else:
    print("Error. Height cannot be negative")