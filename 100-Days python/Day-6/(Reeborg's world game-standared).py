def jump():
    move()
    build_wall()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
for step in range(4):
 jump()

        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
