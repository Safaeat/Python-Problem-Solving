def turn_right():
    turn_left()
    turn_left()
    turn_left()

def wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else: 
        wall()

        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
