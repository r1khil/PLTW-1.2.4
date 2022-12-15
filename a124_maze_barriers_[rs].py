import turtle as trtl

# setup

walls = trtl.Turtle()

walls.hideturtle()

walls.speed(0)

wall_length = 10

wall_width = 10

wall_color = 'black'

wall_count = 1

#function





#excecution

for i in range(25):
  
  if wall_count >4:
    walls.pendown()
    
  else: 
    walls.penup()
  
  walls.left(90)
  
  walls.forward(10)
  
  walls.penup()
  
  walls.forward(wall_width*2)
  
  if wall_count > 4:
    walls.pendown()
  
  
  walls.forward(40)
  
  walls.left(90)
  
  walls.forward(wall_width*2)
  
  walls.back(wall_width*2)
  
  walls.right(90)
  
  walls.forward(wall_length)
  
  
  
  
  
  
  wall_length = wall_length + 10
  
  wall_count = wall_count + 1

walls.hideturtle()












wn = trtl.Screen()
wn.mainloop()