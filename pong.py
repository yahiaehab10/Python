import turtle as t # import turtle module


wm = t.Screen()
wm.title("Pong")
wm.bgcolor("black")
wm.setup(width=800,height=600)
wm.tracer(0)#manually updated

#paddle a
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()#to not draw lines
paddle_a.goto(-350,0)#start pos
#paddle b
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"normal"))

#score
score_a = 0
score_b = 0

#functions
def paddle_a_up():
    y = paddle_a.ycor() #get the coordinate of the paddle a
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #get the coordinate of the paddle a
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #get the coordinate of the paddle a
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #get the coordinate of the paddle a
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wm.listen()
wm.onkeypress(paddle_a_up ,"w")
wm.onkeypress(paddle_a_down ,"s")
wm.onkeypress(paddle_b_up ,"Up")
wm.onkeypress(paddle_b_down ,"Down")

#main game loop
while True:
    wm.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1 #logically as it goes right
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1 #logically as it goes left
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #Win condition
    if score_a == 5:
        pen.clear()
        pen.write("Player A wins",align="center",font=("Courier",24,"normal"))
        break
        

    if score_b == 5:
        pen.clear()
        pen.write("Player B wins",align="center",font=("Courier",24,"normal"))
        
        
