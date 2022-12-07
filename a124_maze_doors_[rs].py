import turtle as trtl

# setup

walls = trtl.Turtle()

wall_length = 10

wall_width = 5

wall_color = 'black'

#function





#excecution

for i in range(25):
  walls.left(90)
  walls.forward(10)
  walls.penup()
  walls.forward(wall_width*2)
  walls.pendown()
  walls.forward(wall_length)
  wall_length = wall_length + 10

walls.hideturtle()












wn = trtl.Screen()
wn.mainloop()