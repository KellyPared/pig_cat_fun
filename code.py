import turtle #turtle library
bob = turtle.Turtle() #instance
kat = turtle.Turtle() #instance
win = turtle.Screen() #instance
win.bgcolor("cyan")

kat.speed(10)
kat.pencolor('black')

#body
kat.penup()
kat.goto(-200,-100)
kat.pendown()
kat.begin_fill()
kat.color('black','peru')
kat.circle(150)
kat.end_fill()

#head
kat.setheading(0)
kat.penup()
kat.goto(-200,100)
kat.pendown()
kat.begin_fill()
kat.color('black','peru')
kat.circle(110)
kat.end_fill()

#nose
kat.setheading(0)
kat.penup()
kat.goto(-200,200)
kat.pendown()
kat.begin_fill()
kat.color('black','misty rose')
kat.left(50)
kat.forward(20)
kat.left(130)
kat.forward(30)
kat.left(130)
kat.forward(24)
kat.end_fill()

#mouth
kat.setheading(270)
kat.pensize(3)
kat.forward(10)
kat.circle(-20, 180)
kat.circle(-20, -180)
kat.circle(20, 180)

#RIGHT EYE

kat.setheading(0)
kat.penup()
kat.goto(-160,220)
kat.pendown()
kat.begin_fill()
kat.color('black','light cyan')
kat.circle(20)
kat.end_fill()
#pupil
kat.setheading(0)
kat.penup()
kat.goto(-160,230)
kat.pendown()
kat.begin_fill()
kat.color('black','saddle brown')
kat.circle(10)
kat.end_fill()

#lefT EYE
kat.setheading(0)
kat.penup()
kat.goto(-240,220)
kat.pendown()
kat.begin_fill()
kat.color('black','light cyan')
kat.circle(20)
kat.end_fill()
#pupil
kat.setheading(0)
kat.penup()
kat.goto(-240,230)
kat.pendown()
kat.begin_fill()
kat.color('black','saddle brown')
kat.circle(10)
kat.end_fill()

#left ear
kat.setheading(0)
kat.penup()
kat.goto(-280,280)
kat.left(95)
kat.pendown()
kat.begin_fill()
kat.color('peru','peru')
kat.forward(60)
kat.right(130)
kat.forward(70)
kat.right(130)
kat.forward(60)
kat.end_fill()

#right ear
kat.setheading(80)
kat.penup()
kat.goto(-120,290)
kat.left(95)
kat.pendown()
kat.begin_fill()
kat.color('peru','peru')
kat.forward(60)
kat.right(130)
kat.forward(70)
kat.right(130)
kat.forward(60)
kat.end_fill()

bob.speed(10)
bob.pencolor("black")
# body
bob.penup()
bob.goto(200,130)
bob.pendown()
bob.begin_fill()
bob.color("black","misty rose")
bob.setheading(180)
bob.circle(150)
bob.end_fill()

# head
bob.penup()
bob.goto(200, 0)
bob.pendown()
bob.begin_fill()
bob.color("black","misty rose")
bob.setheading(0)
bob.circle(100)
bob.end_fill()


## nose
bob.penup()
bob.goto(200,50)
bob.pendown()
bob.setheading(0)
bob.circle(25)


# nostrils
bob.penup()
bob.goto(190,65)
bob.pendown()
bob.setheading(0)
bob.circle(5)
bob.penup()
bob.goto(210,65)
bob.pendown()
bob.circle(5)


# left eye
bob.penup()
bob.goto(170,110)
bob.pendown()
bob.setheading(0)
bob.begin_fill()
bob.color("brown")
bob.circle(10)
bob.end_fill()

# right eye
bob.penup()
bob.goto(230,110)
bob.pendown()
bob.setheading(0)
bob.begin_fill()
bob.color("brown")
bob.circle(10)
bob.end_fill()

# right ear
bob.penup()
bob.goto(240,195)
bob.pendown()
bob.setheading(0)
bob.right(47)
bob.begin_fill()
bob.color("black","misty rose")
for i in range(3):
    bob.forward(70)
    bob.left(127)
bob.end_fill()

# left ear
bob.penup()
bob.goto(160,195)
bob.pendown()
bob.setheading(180)
bob.left(47)
bob.begin_fill()
bob.color("black","misty rose")
for i in range(3):
    bob.forward(70)
    bob.right(127)
bob.end_fill()


# TONGUE
bob.penup()
bob.goto(190,50)
bob.pendown()
bob.setheading(270)
bob.color("red")
bob.begin_fill()
bob.circle(10, 180)
bob.end_fill()






















