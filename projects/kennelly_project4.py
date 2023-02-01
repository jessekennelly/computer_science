"""
Animation with a fish going up and down on the y axis and a crab going side to side on the x axis. When the mouse is clicked
the direction changes

File Name: kennelly_project4.py
Author: Jesse Kennelly
Date: 10/9/22
Course: COMP1351
Assignment: Project 4 - animationw
Collaborators: none
Internet Source: none
"""

import dudraw
dudraw.clear(dudraw.BLUE)
def drawFish(x: int, y: int):

    dudraw.set_pen_color(dudraw.CYAN)
    dudraw.filled_circle(x + .5, y + .5, .04)
    dudraw.filled_triangle(x + .5, y + .5, x + .4, y + .45, x + .4, y +  .55)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_circle(x + .52, y +  .51,  .01)

def drawCrab(x: int, y: int):
    dudraw.set_pen_color(dudraw.RED)
    dudraw.filled_square(x + .5, .04, .04)
    dudraw.filled_rectangle(x + .48, .09, .01, .03)
    dudraw.filled_rectangle(x + .52, .09, .01, .03)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_square(x + .52, .115, .01)
    dudraw.filled_square(x + .48, .115, .01)
    dudraw.set_pen_color(dudraw.RED)
    dudraw.filled_rectangle(x + .44, .02, .03, .01)
    dudraw.filled_rectangle(x + .56, .02, .03, .01)

yVel = .0003
xVel = .0002
x1 = -.2
y1 = .2



while True:
    if dudraw.mouse_pressed() == True:
        xVel *= -1
        yVel *= -1
    
    dudraw.clear(dudraw.BLUE)
    
    drawCrab(x1, .2)
    x1 += xVel
    drawFish(.3, y1)
    y1 += yVel
    dudraw.show()
    if x1 > .5:
        xVel *= -1
    
    if y1 > .5: 
        yVel *= -1
    
    if x1 <= -.5:
        xVel *= -1

    if y1 <= -.5:
        yVel *= -1














dudraw.show(float('inf'))