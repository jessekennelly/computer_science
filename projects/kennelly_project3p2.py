"""
Creates a stick figure with a black head, blue body, and red shoes. It is then manipulated to have chaging position and scaling

File Name: kennelly_project3.py
Author: Jesse Kennelly
Date: 9/27/22
Course: COMP1351
Assignment: Project 3 - scalable and positionable drawing
Collaborators: none
Internet Source: none
"""

from types import DynamicClassAttribute
import dudraw

#sets background to night
dudraw.clear(dudraw.LIGHT_GRAY)

def draw_guy(x: float, y: float, s1: float, s2: float):
    #the value to be added to the current x value of the drawing
    x_position = x

    #the value to be added to the current y value of the drawing
    y_position = y

    #the value to be multiplied to the current value to stretch it on the x axis
    scaleX = s1

    #the value to be multiplied to the currnet value to stretch it on the y axis
    scaleY = s2

    #draws a black head head
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_circle(x_position + scaleX * .5, y_position + scaleY * .5, scaleX * .1)

    #draws a blue body
    dudraw.set_pen_color(dudraw.BLUE)
    dudraw.set_pen_width(.05)
    dudraw.line(x_position + scaleX *.5, y_position + scaleY * .4, x_position + scaleX * .5, y_position + scaleY * .2)

    #draws blue legs
    dudraw.line(x_position + scaleX * .5, y_position + scaleY * .2, x_position + scaleX * .4, y_position + scaleY * .1)
    dudraw.line(x_position + scaleX * .5, y_position + scaleY * .2, x_position + scaleX * .6, y_position + scaleY * .1)

    #draws blue arms
    dudraw.line(x_position + scaleX * .5, y_position + scaleY * .3, x_position + scaleX * .4, y_position + scaleY * .4)
    dudraw.line(x_position + scaleX * .5, y_position + scaleY * .3, x_position + scaleX * .6, y_position + scaleY * .4)
    

    #draws red shoes
    dudraw.set_pen_color(dudraw.RED)

    dudraw.filled_rectangle(x_position + scaleX * .65, y_position + scaleY * .1, scaleX * .09, scaleY * .03)

    dudraw.filled_rectangle(x_position + scaleX * .35, y_position + scaleY * .1, scaleX * .09, scaleY * .03)
    
#draws four stick figures at different shapes and sizes
draw_guy(0.05, 0.05, 0.45, 0.45)
draw_guy(0.05, 0.75, 0.4, 0.1)
draw_guy(0.75, 0.55, 0.1, 0.4)
draw_guy(0.75, 0.25, 0.1, 0.1)
dudraw.show(float('inf'))


   

   




dudraw.show(float('inf'))
