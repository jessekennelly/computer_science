"""


File Name: kennelly_project5.py
Author: Jesse Kennelly
Date: 10/18/22
Course: COMP1351
Assignment: Project 6 - more abstract line art
Collaborators: none
Internet Source: none

Step 1: Create the x and y coordinates for 10 random points on the canvas. These coordinates should be stored in two lists: one for the x-coordinates and one for the y-coordinates.

Step 2: Because the points will be moving, create two more lists of floating point numbers: one for the speeds in the x-direction and one for the speeds in the y-direction. These speeds should be small: recommended values between 0.0 and 0.03 but feel free to experiment once you have the entire program working.

Step 3: Create an animation using a for loop which runs for 100 steps. During each step, several updates are required:

draw a line from each point to the point before it in the coordinate lists. For example, the second point in the coordinate lists should be connected to the first point in the coordinate lists. The third point should be connected to the second point and so on. Note that this means the first point should be connected to the final point in the lists.
update the locations of the points according to the values in the speed lists.
any point which moves beyond a canvas boundary should stop at the boundary and then "bounce" off the boundary on the next step (i.e. change the necessary speed values to make the point bounce).
show the picture for 10 milliseconds
Step 4: After the 100 steps complete, save the resulting picture to a file named Project6Picture and also show it onscreen.

Step 5: Experiment with adding colors, changing the speeds, point locations, length of the animation, etc. to create something interesting.

Step 6: Save the resulting picture and submit the picture.

"""

import dudraw 
import random

x_list = []
y_list = []
x_speed = []
y_speed = []
#populates x list with random floats
for i in range(11):
    x_list.append(random.random())
    y_list.append(random.random())

for i in range(11):
    x_speed.append(random.uniform(.0, .03))
    y_speed.append(random.uniform(.0, .03))

for i in range(100):
    for i in range(9):
        dudraw.line(x_list[i], y_list[i], x_list[i+1], y_list[i+1])
    for i in range(10):
        if x_list[i] <= 0 or x_list[i] >= 1:
            x_speed[i] *= -1
    for i in range(10):
        if y_list[i] <= 0 or y_list[i] >= 1:
            y_speed[i] *= -1
    for i in range(10):
        x_list[i]+= x_speed[i]
        y_list[i] += y_speed[i]
    dudraw.show(10)
    
        
        #dudraw.line(x_list[i], y_list[i], x_list[i+1], y_list[i+1])

dudraw.show(float('inf'))