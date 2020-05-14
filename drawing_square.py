import turtle

def draw_square(brush):
  for i in range(1,5):
    brush.forward(100)
    brush.left(90)
    
def draw_circle(brush):
  brush.circle(100)
  
def draw_canvas():
  canvas = turtle.Screen()
  canvas.bgcolor("black")
  # First Instance of Turtle : square
  brush1 = turtle.Turtle()
  brush1.shape("turtle")
  brush1.color("red")
  brush1.speed(2)
  draw_square(brush1)
  # Second Instance of Turtle : circle
  brush2 = turtle.Turtle()
  brush2.shape("circle")
  brush2.color("white")
  draw_circle(brush2)
  canvas.exitonclick()
draw_canvas()
