import turtle             

# to modify window color
window = turtle.Screen()
window.bgcolor("yellow")

pencil = turtle.Turtle() 

# to draw a star pattern
for i in range(5):
   # to move forward
   pencil.forward(50)  
   # to turn to get a specified shape
   pencil.right(144)  

turtle.done()
