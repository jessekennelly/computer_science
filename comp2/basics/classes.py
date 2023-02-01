class Robot:
    def __init__(self, p1, p2, p3):
        self.fav_saying = p1
        self.age = p2
        self.ready_to_go = p3

my_first_robot = Robot("wow", 52, True)

print(my_first_robot.fav_saying)
print(my_first_robot.age)
print(my_first_robot.ready_to_go)