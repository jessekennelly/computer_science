"""
creates a topographical map of the elevations in colorado

File Name: kennelly_project_9.py
Author: Jesse Kennelly
Date: 11/18/2022
Course: COMP 1351
Assignment: Project 9 - File I/O and 2D lists
Collaborations: None
Internet Source: None
"""
import dudraw

dudraw.set_canvas_size(760,560)
dudraw.set_x_scale(0,760)
dudraw.set_y_scale(0,560)

with open("CO_elevations_feet.txt","r") as f:
    elevations = []
    for line in f:
        #spits each line to be added to internal list
        line = line.rstrip()
        inner_list = line.split(" ")
        #adds internal list to elevations, creating 2d list
        elevations.append(inner_list)

#highest elevation is set to the first element in the list
highest = elevations[0][0]

#goes through each list in 2d list
for innerlist in elevations:
    #goes through the elements within the lists 
    for elevation in innerlist:
        #checks all the values to see which one is the largest
        if int(elevation) > int(highest):
            highest = int(elevation)
print(f"The highest elevation in Colorado is {highest} feet.")

#scale is set to the highest point divided by 255
max = highest/255

def draw_map():
    #starting y value is at the top
    y_val = 560
    for innerlist in elevations:
        #y value is subtracted from and x value is set to 0 when the loop iterates
        y_val -= 1
        x_val = 0

        #This for loop iterates through the given list within elevations. 
        for elevation in innerlist:   
            #division to get the scale similar to the max
            new_elevation = float(elevation)/255
            #the max is divided by the new elevation in the loop to get a value for the rgb
            value = max/new_elevation
            #casted as an int so it will be able to be an rgb value
            rgb_value = int(255/value)
            dudraw.set_pen_color_rgb(rgb_value,rgb_value,rgb_value)
            dudraw.square(x_val+.5,y_val-.5,.5)

            #moves the x position one to the right
            x_val += 1

#variable that will store x and y value of mouse click
clicked_elevation = " "

while True:
    dudraw.clear()
    draw_map()

    if dudraw.mouse_pressed():
        #sets x and y postition of the mouse if it is pressed to values 
        x_value = int(dudraw.mouse_x())
        y_value = int(dudraw.mouse_y())

        #x and y value of the mouse are put into a variable
        clicked_elevation = elevations[y_value][x_value]
    
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_rectangle(730,12,30,12)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.rectangle(730,12,30,12)
    
    #clicked elevation is shown 
    dudraw.set_font_size(25)
    dudraw.text(730,12,f"{clicked_elevation}")
    
    dudraw.show(40)