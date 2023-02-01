from random import random
import dudraw
from dudraw import Color
from math import sqrt

class Circle:
    def __init__(self, x_center, y_center, x_velocity, y_velocity, radius, color):
        self.x_center = x_center
        self.y_center = y_center
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.radius = radius
        self.color = color
        

    def move(self):
        self.x_center += self.x_velocity
        self.y_center += self.y_velocity
        if (self.x_center > 1-self.radius or self.x_center < self.radius):
            self.x_velocity *= -1
        if (self.y_center > 1-self.radius or self.y_center < self.radius):
            self.y_velocity *= -1

    def draw(self):
        dudraw.clear(dudraw.LIGHT_GRAY)
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_center, self.y_center, self.radius)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.x_center, self.y_center, self.radius)
        
    
    def overlaps(self, other):
        #d = sqrt((self.x_center + other.x_center)**2 + (self.y_center + other.y_center)**2)
        #if d <= self.radius + other.radius:
        if self.x_center == other.x_center and self.y_center == other.y_center:
            return True
        else:
            return False

circle1 = Circle(random(), random(), 0.05*random(), 0.05*random(), 0.05, Color(int(random()*256), int(random()*256), int(random()*256)))
circle2 = Circle(random(), random(), 0.05*random(), 0.05*random(), 0.05, Color(int(random()*256), int(random()*256), int(random()*256)))
key = ''
while key != "q":
    circle1.draw()
    dudraw.show(10)
    circle1.move()
    circle2.draw()
    dudraw.show(10)
    circle2.move()

    if circle1.overlaps(circle2) == True:
        dudraw.text(.5, .5, "Crash!")

    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()