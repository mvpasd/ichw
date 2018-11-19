#!/usr/bin/env python3
"""Foobar.py: Description of what foobar does.
__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""
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
def main():
    global x
    while x>=-1:
        s=h[x%6]
        s.speed(0)
        s.shape('circle')
        s.pensize(7)
        s.color(colors[x%6])
        s.penup()
        s.goto((1+x%6)*50*math.sin(x/(100*(1+x%6))),(1+x%6)*60*math.cos(x/(100*(1+x%6))))
        s.pendown()
        s.goto((1+x%6)*50*math.sin((x+1)/(100*(1+x%6))),(1+x%6)*60*math.cos((x+1)/(100*(1+x%6))))
        x=x+1
if __name__ == '__main__':
    main()
  
#另一段代码
   #!/usr/bin/env python3
"""Foobar.py: Description of what foobar does.
__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
""" 
import turtle
import math
turtle.setup(1.0,1.0)
a=turtle.Turtle()
a.dot(80,"yellow")#太阳的大小与颜色
a.penup()
a.fd(65)
a.color('blue')
a.pendown()
a.shapesize(1)
b=turtle.Turtle()
b.penup()
b.fd(90)
b.color('red')
b.pendown()
b.shapesize(1.5)
c=turtle.Turtle()
c.shapesize(1.8)
c.penup()
c.fd(145)
c.color('green')
c.pendown()
d=turtle.Turtle()
d.shapesize(2)
d.penup()
d.fd(190)
d.color('pink')
d.pendown()
e=turtle.Turtle()
e.shapesize(2.1)
e.penup()
e.fd(220)
e.color('orange')
e.pendown()
f=turtle.Turtle()
f.shapesize(2.5)
f.penup()
f.fd(267)
f.color('purple')
f.pendown()
h=[a,b,c,d,e,f]
x=0
def cc(s,r,R,h,l):
    s.speed(0)
    s.shape("circle")
    x=r*math.cos(math.radians(h))
    y=R*math.sin(math.radians(h))
    s.goto(x,y)
    s.shapesize(l)
    s.pensize(6)
def main():
    global x
    while x>=-1:
        cc(a,65,80,10*x,1)
        cc(b,90,123,8*x,1.1)
        cc(c,145,178,6*x,1.3)
        cc(d,190,212,4*x,1.6)
        cc(e,220,236,2*x,1.8)
        cc(f,267,288,x,2.0)
        x=x+1
if __name__ == '__main__':
    main()  

