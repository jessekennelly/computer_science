class Robot:
    mothership = "Star Destroyer"
    def __init__(self, position=(0,0), name="bot", id=0):
        self.position = position 
        self.name = name
        self.id = id
    def say_hello(self):
        print(f"Hi my name is {self.name}.", end=" ")
        print(f"And my position is {self.position}")

    def __str__(self):
        return f"{self.name}, {self.position}"

    def __eq__(self, other):
        return (self.id == other.id and self.position == other.position and self.name == other.name)
   # def destroy_all_humans(self):

    #def go_to_position(self,new_position): 
mybot1 = Robot
mybot2 = Robot
print(mybot1 == mybot2)
print(mybot1.mothership)
print(mybot1)