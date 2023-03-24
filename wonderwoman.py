import turtle

s=turtle.getscreen()
t=turtle.Turtle()
turtle.bgcolor("red")
t.color("yellow")
t.speed(20)

for i in range(2):
    t.penup()
    t.goto(-110,100-80*i)
    t.pendown()

    t.lt(180+240*i)
    t.begin_fill()
    t.fd(110-30*i)
    t.lt(120)
    t.fd(40)
    t.lt(60)
    t.fd(80-30*i)
    t.rt(60)
    t.fd(130)
    t.lt(120)
    t.fd(50)
    
    t.rt(120)
    t.fd(50)
    t.lt(120)
    t.fd(130)
    t.rt(60)
    t.fd(80-30*i)
    t.lt(60)
    t.fd(40)
    t.lt(120)
    t.fd(110-30*i)
    
    t.lt(60)
    t.fd(110)
    t.rt(120)
    t.fd(50)
    t.lt(120)
    t.fd(50)
    t.rt(120)
    t.fd(110)
    t.end_fill()

for i in range(2):
    t.begin_fill()
    t.penup()
    t.goto(270*i-125,57)
    t.pendown()
    t.lt(420)
    t.fd(80)
    t.lt(120-60*i)
    t.fd(35)
    t.lt(60+60*i)
    t.fd(80)
    t.lt(120-60*i)
    t.fd(35)
    t.end_fill()
    
turtle.done()


