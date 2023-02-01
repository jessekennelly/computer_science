"""
Creates canvas where if the mouse is pressed sand will fall randomly down until it hits the floor or other sand. If q is pressed the
window closes
    Filename: kennelly_project3.py
    Author: Jesse Kennelly
    Date: 1/23/23
    Course: COMP1352
    Assignment: Project SandGame - Part 1
    Collaborators: none
    Internet Source: none
"""
import dudraw
from random import randint

#canvas size is same as size of 2d list
dudraw.set_x_scale(0,100)
dudraw.set_y_scale(0,100)
dudraw.set_canvas_size(800,800)
dudraw.set_pen_color_rgb(243,210,186)

#creates list filled with 0
nested_list = []
for i in range(100):
    #each row is its own element 
    row = []
    for j in range(100):
        #row list filled with 100 0's
        row.append(0)
    #row gets appened to larger list, then row value resets
    nested_list.append(row)

#key value to determine when q is pressed, causing it to end while loop
key = ""
while key != "q":
    for row in range(100):
        for col in range(100):
            #checks if any number in the entire 2d list is 0
            if nested_list[row][col] == 1:
                dudraw.filled_square(col ,100-row, .5)

    if dudraw.mouse_is_pressed():
        #stores x and y coordinates in variables
        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())
        #variable for random x position of sand
        x_position = mouse_x + randint(-3,3)
        #variable for random y position of sand
        y_position = 100-mouse_y + randint(-3,3)
        #makes sure sand is within canvas bounds
        if x_position < 100 and x_position > 0:
            if y_position < 100 and y_position > 0:
                #changes number in nested loop to 1/sand value
                nested_list[y_position][x_position] = 1

    for row in range(100,0, -1):
        for colum in range(100):
            #ensures sand falls only if not on the bottom
            if row < 99:
                #checks current sand value with value below it
                if nested_list[row][colum] == 1 and nested_list[row + 1][colum] == 0:
                    #t1 and 0 flip so sand will be drawn in new position
                    nested_list[row + 1][colum] = 1
                    nested_list[row][colum] = 0

    #terminates loop if q is typed
    if dudraw.has_next_key_typed():
        key =  dudraw.next_key_typed()
    dudraw.show(1)
    dudraw.clear()