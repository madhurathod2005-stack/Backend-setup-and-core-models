# i. Classes and Objects
print("Demonstration of Classes and Objects")
# Base class for shapes
class Shape:
 def __init__(self, color="Red"):
 self.color = color

 def display(self):
 print(f"Shape Color: {self.color}")
# Creating an object of the Shape class
shape1 = Shape("Blue")
shape1.display()

