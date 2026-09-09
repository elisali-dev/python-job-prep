import turtle
import random


# create screen
screen = turtle.Screen()
screen.setup(width=600, height=700)
screen.bgcolor("gray")
screen.title("Darren's Car Dodge Game")

# creater the player car 
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.shapesize(stretch_wid=2,stretch_len=1)

player.penup() # do not leave a line on screen if move
player.goto(0,-200)

# create enemey car 
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("red")
enemy.shapesize(stretch_wid=2, stretch_len=1)
enemy.penup()
enemy.goto(0, 280)

# create a writer 
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")

# create a score writer 
score = 0  
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 310)
score_writer.write(
    f"Score: {score}",
    align="center",
    font=("Arial", 18, "normal"),
)

enemy_speed = 10 



LEFT_EDGE = - 280
RIGHT_EDGE = 280 

# define player movement
def move_left():
    new_x = player.xcor() - 20
    new_x = max(new_x, LEFT_EDGE)
    if new_x >= LEFT_EDGE:
        player.setx(new_x)

def move_right():
    new_x = player.xcor() + 20
    new_x = min(new_x, RIGHT_EDGE)
    if new_x <= RIGHT_EDGE: 
        player.setx(new_x)


# make the enemy car move 
def move_enemy():
    global score, enemy_speed
    new_y = enemy.ycor() - enemy_speed
    enemy.sety(new_y)

    if player.distance(enemy) < 30: # 两辆车中心之间的距离 < 30 pixels, 算撞车
            #print("GAME OVER")
            writer.goto(0, 0)
            writer.write(
                "GAME OVER",
                align="center",
                font=("Arial", 28, "bold"),
            )
            return

    if enemy.ycor() < -350:
         score += 1
         enemy_speed += 1

         score_writer.clear()
         score_writer.write(
            f"Score: {score}",
            align="center",
            font=("Arial", 18, "normal"),
         )
         new_x = random.randint(-250, 250)
         enemy.goto(new_x, 350)

    screen.ontimer(move_enemy, 50) # 50 milliseconds 之后，再调用一次 move_enemy()。       

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right") # move_left 代表：把这个 function 本身交给 onkey()，以后用户按键的时候再执行。


move_enemy()
screen.mainloop()