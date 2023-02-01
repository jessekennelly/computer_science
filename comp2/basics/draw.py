import dudraw

while True:
    if dudraw.mouse_is_pressed():
        dudraw.filled_square(dudraw.mouse_x(), dudraw.mouse_y(), 0.1)
    
    dudraw.show()