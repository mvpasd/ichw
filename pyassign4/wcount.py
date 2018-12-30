#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""

import sys
import collections
import urllib.error
from urllib.request import urlopen

def wcount(lines, topn=10):#读取文本，并计算单词出现个数
    doc=urlopen(lines) #进行网络请求
    docstr=doc.read() #读文件
    doc.close() #关闭文件
    jstr=docstr.decode()#转为字符串
    aa=jstr
    for i in jstr:
        if i.isalpha() == False: #将字符串中非字母部分转为空格
            aa=aa.replace(i,' ')
    jstr=aa.lower() #将所有大写字母全部转为小写
    jstrlow=jstr.split() #按空格将其分划
    cc=collections.Counter(jstrlow).most_common(topn) #对其分化出的字母聚集体（单词）计数，并选择其从多到少的前topn位做成列表。
    for i in range(len(cc)):
        print(cc[i][0],end='\t')#打印结果
        print(cc[i][1],end='\n')
def try_out(topn=10):#检查一些运行时常见的错误
    try:
        wcount(sys.argv[1])
    except ValueError:
        print('您输入了错误的网址,请检查并正确输入')
    except urllib.error.HTTPError as e:
        print(e.code,e.reason)
        print('常见错误类型'+'202：请求被接受，.code,e但处理尚未完成 ', '\n'
'204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。','\n'
'301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源','\n'
'302：请求到的资源在一个不同的URL处临时保存',' \n '   
'304 请求的资源未更新','\n' 
'400 非法请求','\n'     
'401 未授权', '\n'   
'403 禁止', '\n'
'404 没有找到','\n'
'5XX 服务器端发现自己出现错误，不能继续执行请求')
    except urllib.error.URLError as e:
        print(e.reason)
        print('网络连接错误，请检查网络连接')
    else:
        wcount(sys.argv[1],topn)
if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    elif len(sys.argv)==2:
        try_out(10)
    else:
        try:
            a=int(sys.argv[2])
        except ValueError:
            print('您未输入正确的数字，请检查并输入')
        else:
            try_out(int(sys.argv[2]))
    

