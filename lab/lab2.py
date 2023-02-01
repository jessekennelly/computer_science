import dudraw

dudraw.set_canvas_size(600, 400)
dudraw.clear(dudraw.YELLOW)

dudraw.set_pen_color(dudraw.RED)
dudraw.filled_triangle(.4, 0, 1, 0, 1, 1)

dudraw.set_pen_color(dudraw.GREEN)
dudraw.filled_triangle(0, 0, 0, 1, .6, 1)

dudraw.show(float('inf'))