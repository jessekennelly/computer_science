from random import random
import dudraw
from dudraw import Color

# main code block:
dudraw.set_canvas_size(400,400)

# create values to represent circle's properties
x_position = random()
y_position = random()
x_velocity = 0.05*random()
y_velocity = 0.05*random()
radius = 0.05
color = Color(int(random()*256), int(random()*256), int(random()*256))

# animation loop, continue until user types 'q'
key = ''
while key != 'q':
    # advance the circle to the next position:
    x_position += x_velocity
    y_position += y_velocity

    # bounce off the edges of the canvas if necessary:
    if (x_position > 1-radius and x_velocity > 0 or
        x_position < radius and x_velocity < 0):
        x_velocity *= -1
    if (y_position > 1-radius and y_velocity > 0 or
        y_position < radius and y_velocity < 0):
        y_velocity *= -1

    # redraw the frame:
    dudraw.clear(dudraw.LIGHT_GRAY)

    # draw the circle at its new position
    dudraw.set_pen_color(color)
    dudraw.filled_circle(x_position, y_position, radius)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.circle(x_position, y_position, radius)

    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

    # display the new frame and pause for 1/20 of a second
    dudraw.show(50)