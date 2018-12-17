#!/usr/bin/env python3

"""tile.py: 解决铺砖方法数.

__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""
import turtle
def brick(h,c,d,a,wall):
    alist=[]
    x=(h+1)%a
    y=(h+1)//a
    for i in range(x,x+c):
        for j in range(y,y+d):
            f=i+j*a-1
            alist.append(f)
            wall[f]=0 
    atuple=tuple(alist)
    return atuple
def qu(h,c,d,a,wall):
    x=(h+1)%a
    y=(h+1)//a
    for i in range(x,x+c):
        for j in range(y,y+d):
            f=i+j*a-1
            wall[f]=f
def pd(a,b,c,d,wall,f):
    if f%a+c>a or f//a+d>b:
        return False
    else:
        ky=True
        for i in range(f,f+c):
            for j in range(i,i+a*d,a):
                if j not in wall:
                    ky=False
        return ky    
def pz(a,b,c,d,wall,f):
    all_ans=[]
    if f==a*b:
        return[[]]
    while f not in wall:
        f+=1
        if f==a*b:
            return[[]]
    for (c,d) in [(c,d),(d,c)]:
        if pd(a,b,c,d,wall,f) is True:
            atuple=brick(f,c,d,a,wall)
            ans=pz(a,b,c,d,wall,f+1)
            for i in ans:
                i.append(atuple)
            all_ans.extend(ans)
            qu(f,c,d,a,wall)
    return all_ans
a=int(input('请输入墙壁长度(整数)：'))
b=int(input('请输入墙壁高度(整数)：'))
c=int(input('请输入砖的长度(整数)：'))
d=int(input('其输入砖的宽度(整数)：'))
if a*b % (c*d)==0:
    print('您所选择的砖符合要求')
else:
    print('您所选择的砖不符合要求')
wall=[]
for i in range(0,a*b):
    wall.append(i)
def pdpd(a,b,c,d,wall,f=0):
    all_ans=pz(a,b,c,d,wall,f=0)
    if c==d:
        ans=list(all_ans[0])
        all_ans=[ans]
    return all_ans
def ksh(all_ans):
    global a,b,c,d
    bh=len(all_ans)
    turtle.setup(0.9,0.9)
    hb=turtle.Turtle()
    hb.ht()
    turtle.title('将选择的方案可视化')
    fn=int(turtle.numinput('请选择方案','方案可选编号:1--'+str(bh),1,1,bh))
    fn=fn-1
    fn=all_ans[fn]
    hb.speed(0)
    turtle.setworldcoordinates(-a/4,-b/4,a*5/4,b*5/4)
    for i in range(2):
        hb.forward(a)
        hb.left(90)
        hb.forward(b)
        hb.left(90)
    for i in range(1,a):
        hb.penup()
        hb.goto(i,0)
        hb.pendown()
        hb.goto(i,b)
    for i in range(1,b):
        hb.penup()
        hb.goto(0,i)
        hb.pendown()
        hb.goto(a,i)
    hb.pensize(6)
    if c*d!=1:
        for i in fn:
            hb.color('blue')
            x1=(i[0])%a
            y1=(i[0])//a
            x2=(i[c*d-1])%a+1
            y2=(i[c*d-1])//a+1
            hb.penup()
            hb.goto(x1,y1)
            hb.pendown()
            hb.goto(x1,y2)
            hb.goto(x2,y2)
            hb.goto(x2,y1)
            hb.goto(x1,y1)
    else:
        for i in fn:
            hb.color('red')
            x1=(i[0])%a
            y1=(i[0])//a
            x2=x1+1
            y2=x2+1
            hb.penup()
            hb.goto(x1,y1)
            hb.pendown()
            hb.goto(x2,y1)
            hb.goto(x2,y2)
            hb.goto(x1,y2)
            hb.goto(x1,y1)
    for i in range(a*b):
        x=i%a
        y=i//a
        hb.penup()
        hb.goto(x+1/2,y+1/2)
        hb.write(i,False,'center')
def main():
    all_ans=pdpd(a,b,c,d,wall,f=0)
    print('有',len(all_ans),'种方案',all_ans)
    ksh(all_ans)
if __name__ == '__main__':
    main()

