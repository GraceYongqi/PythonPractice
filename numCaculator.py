#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : numCaculator.py
@Author: Grace
@Date  : 2018/7/16
@Desc  : 核心编程5.9数字类型变量练习 p97
'''

# import modules
import re
from prettytable import PrettyTable
import random
# global variables

# class definition

# function definition
def multiply(a, b):
    '返回a和b的乘积'
    return a*b

def mod(a, b):
    '返回a除以b的余数'
    return a%b

def judgeLeap(year):
    '判断是否为闰年'
    if mod(year, 4)==0 and mod(year, 100)!=0:
        return True
    else:
        return False

def division(x, y ):
    return divmod(x, y)

def coinConversion(x, res,y):
    '共有1、5、10、25四种美分硬币，找出x美元换算硬币最少的方法'
    if x > 25:
        y = 25
    elif x > 10:
        y = 10
    elif x > 5:
        y = 5
    elif x >= 1:
        y = 1
    else:
        return
    divres = division(x, y)
    a = y
    b = divres[0]
    res.append([a,b])
    coinConversion(divres[1],res,y)
    return

def conversionRes():
    '输出硬币换算结果'
    x = float(raw_input('换算x美元：'))
    result = []
    coinConversion(int(x*100), result,0)
    return result

def CalculateBySplit(str):
    '输入表达式返回结果'
    operands = re.split(r'\+|-|\/|\*\*|\*',str)
    tmp = re.split(operands[0],str)
    operator = re.split(operands[1],tmp[1])
    a = int(operands[0])
    b = int(operands[1])
    if operator[0]=='+':
        return a+b
    elif operator[0]=='-':
        return a-b
    elif operator[0]=='*':
        return a*b
    elif operator[0]=='/':
        return a/b
    elif operator[0]=='**':
        return a**b
    else:
        return None

def EuclideanAlgorithm(x,y):
    '利用欧几里得算法即辗转相除法得到最大公约数'
    if y!=0:
        r = x%y
        x = y
        y = r
        return EuclideanAlgorithm(x,y)
    else:
        return x

def FinanceCalculator():
    '输入初始金额和月开销数，返回剩下的金额、当月的支出数、和最后的支出数(表格形式输出）'
    print 'Enter opening balance:',
    RawBalance = float(raw_input())
    Balance = RawBalance
    print 'Enter monthly payment:',
    MonthlyPayment = float(raw_input())

    print '\t\tAmount\tRemaining'
    table = PrettyTable(['Pymt#','Paid','Balance'])
    table.add_row(['---','---','---------'])
    i = 0
    while Balance>0:
        if i==0:
            paid = 0.00
        elif i>0 and Balance>=MonthlyPayment:
            paid = MonthlyPayment
        else:
            paid = Balance
        Balance = Balance-paid
        table.add_row([i,'$%.2f' % paid,'$%.2f' % Balance])
        i+=1
    table.sort_key(i)
    table.reversesort=False
    table.border = 0
    print table

def FetchRandom():
    '生成随机数列表并从中抓取'
    N1 = random.randint(2,100)
    N2 = random.randint(1,100)
    while N2>N1:
        N2 = random.randint(1,100)
    alist = []
    for i in range(N1):
        n = random.randint(0, 2 ^ 31 - 1)
        alist.append(n)
    blist = []
    for i in range(N2):
        blist.append(random.choice(alist))
    print sorted(blist)
    print 'N1=',N1,' N2=',N2,' n=',n



# main function
if __name__ == '__main__':
    pass
