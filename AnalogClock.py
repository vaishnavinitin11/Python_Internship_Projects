from turtle import Turtle,Screen
import datetime

window=Screen()
window.title('Analog Digital Clock')
window.bgcolor('black')
window.setup(width=1000,height=800)

circle=Turtle()
circle.penup()
circle.pencolor('#118893')
circle.speed(0)
circle.pensize(25)
circle.hideturtle()
circle.goto(0,-390)
circle.pendown()
circle.fillcolor('#17202A')
circle.begin_fill()
circle.circle(400)
circle.end_fill()

hHand=Turtle()
hHand.shape('arrow')
hHand.color('white')
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4,stretch_len=18)

mHand=Turtle()
mHand.shape('arrow')
mHand.color('white')
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4,stretch_len=26)

sHand=Turtle()
sHand.shape('arrow')
sHand.color('dark red')
sHand.speed(0)
sHand.shapesize(stretch_wid=0.4,stretch_len=36)

centerCircle=Turtle()
centerCircle.shape('circle')
centerCircle.color('white')
centerCircle.shapesize(stretch_wid=1.5,stretch_len=1.5)

pen = Turtle()
pen.speed(0)
pen.color('white')

pen.penup()
pen.hideturtle()
pen.goto(170,260)
pen.write('1',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(300,140)
pen.write('2',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(340,-30)
pen.write('3',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(300,-200)
pen.write('4',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(170,-325)
pen.write('5',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(0,-370)
pen.write('6',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(-170,-325)
pen.write('7',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(-300,-200)
pen.write('8',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(-340,-30)
pen.write('9',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(-280,140)
pen.write('10',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(-160,260)
pen.write('11',align='center',font=('Algerian',50,'bold'))

pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write('12',align='center',font=('Algerian',50,'bold'))

def movehHand():
    currentHourInterval=datetime.datetime.now().hour
    degree=(currentHourInterval-15)* -30
    currentMinuteInterval=datetime.datetime.now().minute
    degree=degree + -0.5 * currentMinuteInterval
    hHand.setheading(degree)
    window.ontimer(movehHand,60000)

def movemHand():
    currentMinuteInterval=datetime.datetime.now().minute
    degree=(currentMinuteInterval-15)* -6
    currentSecondInterval=datetime.datetime.now().second
    degree=degree + (-currentSecondInterval * 0.1)
    mHand.setheading(degree)
    window.ontimer(movemHand,1000)

def movesHand():
    currentSecondInterval=datetime.datetime.now().second
    degree=(currentSecondInterval - 15)* -6
    sHand.setheading(degree)
    window.ontimer(movesHand,1000)
    

window.ontimer(movehHand,1)
window.ontimer(movemHand,1)
window.ontimer(movesHand,1)
window.exitonclick()