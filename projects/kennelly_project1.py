"""
Using dudraw to create a scene with a mountain at night with a moon and
a flag. The mountain and moon are contained in one function, and the flag 
is contained in another. 

File Name: kennelly_project1.py
Author: Jesse Kennelly
Date: 9/15/22
Course: COMP1351
Assignment: Project 1 - Create a Drawing
Collaborators: none
Internet Source: none
"""

import dudraw

dudraw.set_canvas_size(600, 400)

#sets background to night
dudraw.clear(dudraw.BLACK)
def draw_mountain():

    #creates the background of the mountain
    dudraw.set_pen_color(dudraw.LIGHT_GRAY)
    dudraw.filled_triangle(0, 0, 1, 0, .5, 1)

    #adds the snow to the top of the mountain
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_triangle(.37, .75, .63, .75, .5, 1)

    #creates moon base
    dudraw.filled_circle(.9, .9, .05)

    #creates moon craters
    dudraw.set_pen_color(dudraw.GRAY)
    dudraw.filled_circle(.92, .92, .012)
    dudraw.filled_circle(.93, .89, .008)
    dudraw.filled_circle(.87, .9, .013)
   

   
#draws a flag
def draw_flag():
    dudraw.set_pen_color(dudraw.BLACK)
    #draw flag pole
    dudraw.line(.5, .78, .5, .85)

    #draws flag body
    dudraw.set_pen_color(dudraw.GREEN)
    dudraw.filled_rectangle(.53, .85, .03, .03)

#this function puts both drawings (mountain and flag) into one so they can both show
def show_drawing():
    draw_mountain()
    draw_flag()
    dudraw.show(float('inf'))

show_drawing()



