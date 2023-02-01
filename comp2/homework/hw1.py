import dudraw

dudraw.set_canvas_size(400,400)
dudraw.set_x_scale(0, 4)
dudraw.set_y_scale(0, 4)
dudraw.clear(dudraw.LIGHT_GRAY)
dudraw.set_pen_color(dudraw.WHITE)

for i in range(4):
    for j in range(4-i):
        dudraw.filled_circle(j + 0.5, i + 0.5, 0.5)
        dudraw.show(1000)
dudraw.show(float("inf"))