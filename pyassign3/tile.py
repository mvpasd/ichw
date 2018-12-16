#!/usr/bin/env python3

"""tile.py: 解决铺砖方法数.

__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""
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
b=int(input('请输入墙壁宽度(整数)：'))
c=int(input('请输入砖的长度(整数)：'))
d=int(input('其输入砖的宽度(整数)：'))
if a*b % (c*d)==0:
    print('您所选择的砖符合要求')
else:
    print('您所选择的砖不符合要求,将会报错')
wall=[]
for i in range(0,a*b):
    wall.append(i)
def pdpd(a,b,c,d,wall,f=0):
    all_ans=pz(a,b,c,d,wall,f=0)
    if c==d:
        ans=list(all_ans[0])
        all_ans=[ans]
        print(all_ans)
    return all_ans
all_ans=pdpd(a,b,c,d,wall,f=0)
print(len(all_ans))
