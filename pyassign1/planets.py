import turtle
import math
turtle.setup(1.0,1.0)
a=turtle.Turtle()
a.shapesize(1)
b=turtle.Turtle()
b.shapesize(1.5)
c=turtle.Turtle()
c.shapesize(1.8)
d=turtle.Turtle()
d.shapesize(2)
e=turtle.Turtle()
e.shapesize(2.1)
f=turtle.Turtle()
f.shapesize(2.5)
h=[a,b,c,d,e,f]
a.dot(80,"yellow")#太阳的大小与颜色
colors=['blue','green','red','black','orange','cornflowerblue'] #行星的颜色
x=0
while x>=-1:
    s=h[x%6]
    s.speed(0)
    s.shape('circle')
    s.pensize(7)
    s.color(colors[x%6])
    s.penup()
    s.goto((1+x%6)*50*math.sin(x/(1000*(1+x%6))),(1+x%6)*60*math.cos(x/(1000*(1+x%6))))
    s.pendown()
    s.goto((1+x%6)*50*math.sin((x+1)/(100*(1+x%6))),(1+x%6)*60*math.cos((x+1)/(1000*(1+x%6))))
    x=x+1
