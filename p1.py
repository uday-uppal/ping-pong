from tkinter import font
import turtle

from sympy import true

wn=turtle.Screen()
wn.title("udays first game")
wn.bgcolor("blue")
wn.setup(height=600, width=800)
wn.tracer(0)
score_a=0
score_b=0
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx=0.2
ball.dy=-0.2

pen=turtle.Turtle()
pen.speed(0)
pen.color="white"
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0  Player B : 0", align="center", font=("times new roman", 24, "normal"))

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

wn.listen()    
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
while true:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if(ball.ycor()>290):
        ball.sety(290)
        ball.dy*=-1

    if(ball.ycor()<-290):
        ball.sety(-290)
        ball.dy*=-1
    if(ball.xcor()<-390):
        ball.setx(-390)
        ball.dx*=-1    
    if(ball.xcor()>390):
        ball.setx(390)
        ball.dx*=-1    
    if((ball.ycor()<paddle_b.ycor()+40) and (ball.ycor()>paddle_b.ycor()-40) and (ball.xcor()>340) and (ball.xcor()<350)):
        ball.dx*=-1
    if((ball.ycor()<paddle_a.ycor()+40) and (ball.ycor()>paddle_a.ycor()-40) and (ball.xcor()<-340) and (ball.xcor()>-350)):
        ball.dx*=-1
    if(paddle_a.ycor()+50>300):
       paddle_a.sety(250)
        
    if(paddle_b.ycor()+50>300):
       paddle_b.sety(250)
    if(paddle_a.ycor()-50<-300):
       paddle_a.sety(-250)
    if(paddle_b.ycor()-50<-300):
        paddle_b.sety(-250)   