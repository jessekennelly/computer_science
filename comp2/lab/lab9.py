from __future__ import annotations
from random import random
import dudraw
from dudraw import Color
import math

# class to manage an animated circle
class BouncingCircle:
    # client gives initial (x, y) position of center of circle, initial
    # (xv, yv) velocity of the circle, and radius. This constructor 
    # initializes the color to a random value
    def __init__(self, x: float, y: float, xv: float, yv: float, r: float):
        self.x_position = x
        self.y_position = y
        self.x_velocity = xv
        self.y_velocity = yv
        self.radius = r
        self.color = Color(int(256*random()), int(256*random()), int(256*random()))
    
    # advance the position of the circle, based on the velocity. If the circle
    # escapes the [0, 1]x[0, 1] canvas, then reverse the direction to bounce off the
    # walls.
    def move(self):
        # advance the circle to the next position:
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity
        
        # bounce off the edges of the canvas if necessary:
        if (self.x_position > 1-self.radius and self.x_velocity > 0 or 
            self.x_position < self.radius and self.x_velocity < 0):
            self.x_velocity *= -1
        if (self.y_position > 1-self.radius and self.y_velocity > 0 or 
            self.y_position < self.radius and self.y_velocity < 0):
            self.y_velocity *= -1 
    
    # redraw the circle, using the given position and color. Draw a black
    # outline around the edge of the circle
    def draw(self):
        # draw the circle at its new position
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.radius)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.x_position, self.y_position, self.radius)
        
    # return True/False depending if this circle and the second circle (other)
    # passed as a parameter are intersecting.
    def overlaps(self, other: BouncingCircle)->bool:
        # The circles overlap if the distance between their centers is less than the
        # sum of their radii
        distance = math.sqrt((self.x_position- other.x_position)**2 + (self.y_position-other.y_position)**2)
        return distance < self.radius+other.radius
   
    # reset the color to a new random value
    def random_color(self):
        self.color = Color(int(256*random()), int(256*random()), int(256*random()))

# main code block:
dudraw.set_canvas_size(400,400)

# create two circles at random positions, with a random velocity between 0 and 0.05
# and a fixed radius of 0.06
circle_1 = BouncingCircle(random(), random(), random()*0.05, random()*0.05, 0.06)
circle_2 = BouncingCircle(random(), random(), random()*0.05, random()*0.05, 0.06)


# animation loop, continue until user types 'q'
key = ''
my_circles = []
for i in range(6):
    my_circles.append(BouncingCircle(random(), random(), random()*0.001, random()*0.001, 0.06))
while key != 'q':
    
    # advance circles to their new position
    for circle in my_circles:
        circle.move()

    # redraw the frame, by refreshing the background then redrawing each circle
    dudraw.clear(dudraw.WHITE)
    for circle in my_circles:
        circle.draw()

    # detect any key presses (used to quit the program)
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

    # flash with new random colors as long as the circles intersect
    
    
    for i in range(len(my_circles)):
        for j in range(i +1, len(my_circles)):
            if my_circles[i].overlaps(my_circles[j]):
                my_circles[i].random_color()
                my_circles[j].random_color()

    # display the new frame and pause for 1/20 of a second
    dudraw.show(1)

