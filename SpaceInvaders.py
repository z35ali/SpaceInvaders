#Imports 
import turtle
import os
import random
import math

#import module
import winsound


#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

#Set up screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


#Draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup();
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score=0

#Draw score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("red")
score_pen.penup()
score_pen.setposition(-290,270)
scorestring="Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#Create the player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed=15


#Choose number of enemies
number_of_enemies=10
#Creates an empty lit
enemies=[]

#Add enemies to list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
enemyspeed=10


    

#Creat the player's bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=40

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate="fire"

#Move the player horizontally
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)
    
def fire_bullet():
    #Declare bulletstate as a global
    global bulletstate
    if bulletstate=="ready":
        #Play laser sound
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        
        bulletstate="fire"
        #Move the bullet to just above the player
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<20:
        winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
        return True
    else:
        return False

    
#Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet,"space")

#Main game loop
while True:
    for enemy in enemies:
        #Move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor()>280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *=-1
            
        if enemy.xcor()<-280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
        #Check for collision 
        if isCollision(bullet,enemy):
                #Reset bullet
                bullet.hideturtle()
                bulletstate="ready"
                bullet.setposition(0,-400)
                #Reset the enemy
                x=random.randint(-200,200)
                y=random.randint(100,250)
                enemy.setposition(x,y)
                #Update score
                score+=10
                score_pen.clear()
                scorestring="Score: %s" %score
                score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

                    

        if isCollision(player,enemy):
                player.hideturtle()
                for e in enemies:
                    e.hideturtle()
                winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
                gameover_pen=turtle.Turtle()
                gameover_pen.penup()
                gameover_pen.speed(0)
                gameover_pen.color("red")
                gameover_pen.setposition(0,0)
                gameover_pen.write("GAME OVER",False,align="center",font=("Arial",20,"normal"))
                player.setposition(0, 550)
                gameover_pen.hideturtle()
                break
    
    #Move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #Check to see if bullet is at top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
                                   
            







        

