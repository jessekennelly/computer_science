"""
Draws a grid of orange lines on a red background with cyan circles at the meeting points of lines in the grid.

File Name: kennelly_project5.py
Author: Jesse Kennelly
Date: 10/13   /22
Course: COMP1351
Assignment: Project 5 - optical illusions
Collaborators: none
Internet Source: none
"""

import dudraw
dudraw.clear(dudraw.RED)

def drawline(x1: int, y1: int, x2: int, y2: int):
    """
    This function draws an orange line at points inputed when calling the function, allowing for easy manipulation in for-loops
    """
    dudraw.set_pen_width(.02)
    dudraw.set_pen_color(dudraw.ORANGE)
    dudraw.line(x1 + 0, y1 + 0, x2 + 0, y2 + 0)


#draws lines across the y axis (down to up)
x1 = 0
x2 = 1
y1 = 0
y2 = 0
for i in range(9):
    drawline(x1, y1, x2, y2)
    y1 += .12
    y2 += .12

#draws lines across the x axis (left to right)
xA = 0
xB = 0
yA = 0
yB = .95
for j in range(9):
    drawline(xA, yA, xB, yB)
    xA += .125
    xB += .125




cX = .125
cY = .84
#draws the colums of circles
for i in range(7):
    #draws the rows of circles
    for j in range(7):
        dudraw.set_pen_color(dudraw.CYAN)
        dudraw.filled_circle(cX, cY, .01)
        cX += .125
    cX = .125
    cY -= .12

dudraw.show(float('inf'))