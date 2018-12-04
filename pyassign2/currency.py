#!/usr/bin/env python3

"""currency.py: Description of what currency does.
__author__ = "He Zeyu"
__pkuid__  = "1800011821"
__email__  = "1800011821@pku.edu.cn"
"""
from urllib.request import urlopen
def ss(x,y,z):
    #通过网站进行货币转换
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+x+'&to'+'='+y+'&amt'+'='+str(z))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr
def cccc(jstr):
    #对从网站上得来的结果处理使符合要求
    d=int(jstr.index(','))
    c=jstr[d:]
    e=int(c.index(':'))    
    cc=c[e:]
    f=int(cc.index(','))
    ccc=cc[2:f]
    return ccc
def exchange(currency_from, currency_to, amount_from):
    #货币转换并得到所需输出结果
    jstr=ss(currency_from, currency_to, amount_from) 
    ccc=cccc(jstr)
    print(ccc)
def test_ss():
    #测试货币转换模块
    jstr=ss('USD','EUR',2.5)
    assert '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'==jstr
def test_cccc():
    #测试结果处理模块
    jstr=ss('USD','EUR',2.5)
    ccc=cccc(jstr)
    assert '''"2.1589225 Euros"'''==ccc
def test_exchange():
    #测试exchange函数
    jstr=ss('USD','EUR',2.5)
    ccc=cccc(jstr)
    assert '''"2.1589225 Euros"'''==ccc
def test_all():
    #测试所有模块
    test_ss()
    test_cccc()
    test_exchange()
    print("All tests passed")
def main():
    test_all()
    print('可以转换的货币缩写请自行查询网站http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php#service’)
    currency_from=str(input('要转换的货币是:',))
    currency_to=str(input('转化后的货币是:',))
    amount_from=str(input('数值:',))
    exchange(currency_from, currency_to, amount_from)
if __name__ == '__main__':
    main()   
