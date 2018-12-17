#!/usr/bin/env python3

"""tile.py: 解决铺砖方法数.
__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""
import turtle
def brick(h,c,d,a,wall):
    '''对于被铺上砖的区域，将其状态记为0，并将砖块打包进入atuple '''
    alist=[]
    x=(h+1)%a #将单位区域的标记数转换为二维坐标
    y=(h+1)//a
    for i in range(x,x+c):
        '''将从标记数为h的单位区域的右上角铺上砖 '''
        for j in range(y,y+d):
            f=i+j*a-1
            alist.append(f) #将砖打包进alist
            wall[f]=0 
    atuple=tuple(alist)
    return atuple
def qu(h,c,d,a,wall):
    '''对已铺上砖的区域清掉，区域状态变为其标记数h '''
    x=(h+1)%a #转为二维坐标
    y=(h+1)//a
    for i in range(x,x+c):
        for j in range(y,y+d):
            f=i+j*a-1
            wall[f]=f
def pd(a,b,c,d,wall,f):
    '''pd,判断谐音。判断区域是否可铺 '''
    if f%a+c>a or f//a+d>b:
        return False #铺出墙外的情况
    else:
        ky=True
        for i in range(f,f+c):
            for j in range(i,i+a*d,a):
                if j not in wall:
                    ky=False #其右上角部分区域已被铺上的情况
        return ky    
def pz(a,b,c,d,wall,f):
    '''铺砖谐音，递归铺砖至铺满墙，f为单位区域的标记数 范围从0至a*b-1'''
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
def pdpd(a,b,c,d,wall,f=0):
    '''由于砖为正方形时实际只有一种铺法，故在判断一次砖是否为正方形'''
    all_ans=pz(a,b,c,d,wall,f=0)
    if c==d:
        ans=list(all_ans[0])
        all_ans=[ans]
    return all_ans
def ksh(all_ans,a,b,c,d):
    '''可视化谐音，选择某种方法进行可视化'''
    bh=len(all_ans) #方法总数
    turtle.setup(0.9,0.9)
    hb=turtle.Turtle()
    turtle.title('将选择的方案可视化')
    fn=int(turtle.numinput('请选择方案','方案可选编号:1--'+str(bh),1,1,bh))
    fn=fn-1 #由于list从零开始，而非从一开始，故减一
    fn=all_ans[fn] #将方法取出
    hb.speed(0)
    turtle.setworldcoordinates(-a/4,-b/4,a*5/4,b*5/4)
    for i in range(2): #画出墙
        hb.forward(a)
        hb.left(90)
        hb.forward(b)
        hb.left(90)
    for i in range(1,a): #画出区域
        hb.penup()
        hb.goto(i,0)
        hb.pendown()
        hb.goto(i,b)
    for i in range(1,b): #画出区域
        hb.penup()
        hb.goto(0,i)
        hb.pendown()
        hb.goto(a,i)
    hb.pensize(6)
    #!/usr/bin/env python3

"""tile.py: 解决铺砖方法数.
__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""
import turtle
def brick(h,c,d,a,wall):
    '''对于被铺上砖的区域，将其状态记为0，并将砖块打包进入atuple '''
    alist=[]
    x=(h+1)%a #将单位区域的标记数转换为二维坐标
    y=(h+1)//a
    for i in range(x,x+c):
        '''将从标记数为h的单位区域的右上角铺上砖 '''
        for j in range(y,y+d):
            f=i+j*a-1
            alist.append(f) #将砖打包进alist
            wall[f]=0 
    atuple=tuple(alist)
    return atuple
def qu(h,c,d,a,wall):
    '''对已铺上砖的区域清掉，区域状态变为其标记数h '''
    x=(h+1)%a #转为二维坐标
    y=(h+1)//a
    for i in range(x,x+c):
        for j in range(y,y+d):
            f=i+j*a-1
            wall[f]=f
def pd(a,b,c,d,wall,f):
    '''pd,判断谐音。判断区域是否可铺 '''
    if f%a+c>a or f//a+d>b:
        return False #铺出墙外的情况
    else:
        ky=True
        for i in range(f,f+c):
            for j in range(i,i+a*d,a):
                if j not in wall:
                    ky=False #其右上角部分区域已被铺上的情况
        return ky    
def pz(a,b,c,d,wall,f):
    '''铺砖谐音，递归铺砖至铺满墙，f为单位区域的标记数 范围从0至a*b-1'''
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
def pdpd(a,b,c,d,wall,f=0):
    '''由于砖为正方形时实际只有一种铺法，故在判断一次砖是否为正方形'''
    all_ans=pz(a,b,c,d,wall,f=0)
    if c==d:
        ans=list(all_ans[0])
        all_ans=[ans]
    return all_ans
def ksh(all_ans,a,b,c,d):
    '''可视化谐音，选择某种方法进行可视化'''
    bh=len(all_ans) #方法总数
    turtle.setup(0.9,0.9)
    hb=turtle.Turtle()
    turtle.title('将选择的方案可视化')
    fn=int(turtle.numinput('请选择方案','方案可选编号:1--'+str(bh),1,1,bh))
    fn=fn-1 #由于list从零开始，而非从一开始，故减一
    fn=all_ans[fn] #将方法取出
    hb.speed(0)
    turtle.setworldcoordinates(-a/4,-b/4,a*5/4,b*5/4)
    for i in range(2): #画出墙
        hb.forward(a)
        hb.left(90)
        hb.forward(b)
        hb.left(90)
    for i in range(1,a): #画出区域
        hb.penup()
        hb.goto(i,0)
        hb.pendown()
        hb.goto(i,b)
    for i in range(1,b): #画出区域
        hb.penup()
        hb.goto(0,i)
        hb.pendown()
        hb.goto(a,i)
    hb.pensize(6)
    for i in fn: #铺砖
        hb.color('blue')
        x1=(i[0])%a
        y1=(i[0])//a
        x2=(i[c*d-1])%a+1
        y2=(i[c*d-1])//a+1 #确定砖的四角坐标
        hb.penup()
        hb.goto(x1,y1)
        hb.pendown()
        hb.goto(x1,y2)
        hb.goto(x2,y2)
        hb.goto(x2,y1)
        hb.goto(x1,y1) #铺砖
    for i in range(a*b): #加上单位区域的标记数
        x=i%a
        y=i//a
        hb.penup()
        hb.goto(x+1/2,y+1/2)
        hb.write(i,False,'center')
    hb.ht()
def main():
    a=int(input('请输入墙壁长度(整数)：'))
    b=int(input('请输入墙壁高度(整数)：'))
    c=int(input('请输入砖的长度(整数)：'))
    d=int(input('其输入砖的宽度(整数)：'))
    if a*b % (c*d)==0:
        print('您所选择的砖符合要求')
    else:
        print('您所选择的砖不符合要求，会报错')
    wall=[]
    for i in range(0,a*b):
        wall.append(i)
    all_ans=pdpd(a,b,c,d,wall,f=0)
    print('有',len(all_ans),'种方案',all_ans)
    ksh(all_ans,a,b,c,d)
if __name__ == '__main__':
    main()
    for i in fn: #铺砖
        x1=(i[0])%a
        y1=(i[0])//a
        x2=(i[c*d-1])%a+1
        y2=(i[c*d-1])//a+1 #确定砖的四角坐标
        hb.penup()
        hb.goto(x1,y1)
        hb.pendown()
        hb.goto(x1,y2)
        hb.goto(x2,y2)
        hb.goto(x2,y1)
        hb.goto(x1,y1) #铺砖
    for i in range(a*b): #加上单位区域的标记数
        x=i%a
        y=i//a
        hb.penup()
        hb.goto(x+1/2,y+1/2)
        hb.write(i,False,'center')
    hb.ht()
def main():
    a=int(input('请输入墙壁长度(整数)：'))
    b=int(input('请输入墙壁高度(整数)：'))
    c=int(input('请输入砖的长度(整数)：'))
    d=int(input('其输入砖的宽度(整数)：'))
    if a*b % (c*d)==0:
        print('您所选择的砖符合要求')
    else:
        print('您所选择的砖不符合要求，会报错')
    wall=[]
    for i in range(0,a*b):
        wall.append(i)
    all_ans=pdpd(a,b,c,d,wall,f=0)
    print('有',len(all_ans),'种方案',all_ans)
    ksh(all_ans,a,b,c,d)
if __name__ == '__main__':
    main()
