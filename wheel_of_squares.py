import turtle

def draw_square(brush):
  for i in range(1,5):
    brush.forward(100)
    brush.left(90)
  
def draw_canvas():
  canvas = turtle.Screen()
  canvas.bgcolor("black")
  # Instance of Turtle : square
  brush1 = turtle.Turtle()
  brush1.shape("turtle")
  brush1.color("red")
  brush1.speed(10)
  for i in range(1,73): # runs the loop 72 times
    draw_square(brush1)
    brush1.left(5)
  canvas.exitonclick()
draw_canvas()
