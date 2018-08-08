#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : seqPractice.py
@Author: Grace
@Date  : 2018/7/30
@Desc  : 第六章序列的习题实现160
'''

# import modules
import string
import keyword
import copy
import random

ERROR = -1
# function definition
def idChecher(idstr):
    '检查标识符是否符合规则，排除了关键字'
    alphas = string.letters+'_'
    nums = string.digits
    length = len(idstr)
    alphanum = alphas+nums

    if idstr[0] not in alphas:
        print 'invalid: the first symbol must be a letter or _'
        return False
    if length>1:
        if idstr in keyword.kwlist:
            print 'invalid: symbol cannot be a keyword'
            return False
        for otherchar in idstr[1:]:
            if otherchar not in alphanum:
                print 'invalid: other symbols must be numbers, letters, or _'
                return False
        return True
    else:
        return True

def palindromeJudge(str):
    '判断字符串是否重现，除了严格的回文串之外，还支持空格等符号'
    length = len(str)
    for i in range(length):
        j = length-1-i
        if i> j:
            break
        if str[i] != str[j]:
            return False
    return True

def palindromeGenerator(str):
    '利用输入的字符串生成回文串'
    print str+str[::-1] #或者 str[-length:]

def stripSub(str):
    'strip()的替代函数，去掉字符串的前后空格'
    precount = sucount = 0
    length = len(str)

    while True:
        if str[precount]==' ':
            precount +=1
        else:
            break
    while True:
        if str[-sucount] == ' ':
            sucount +=1
        else:
            break
    end = length - sucount+1
    str = str[precount:end]
    return  str

def integerToIP(integer):
    raw = bin(int(integer)).lstrip('0b').zfill(32)
    print raw
    ip = '%d.%d.%d.%d' % (int(raw[0:8],2) , int(raw[8:16],2) , int(raw[16:24],2) , int(raw[24:32],2))
    return ip

def ipToInteger(ip):
    raw = ip.split('.')
    if len(raw)!=4:
        print '不是合法的IP地址，请重新输入'
        return
    binnum = bin(int(raw[0])).lstrip('0b').zfill(8)+\
             bin(int(raw[1])).lstrip('0b').zfill(8)\
             +bin(int(raw[2])).lstrip('0b').zfill(8)+\
             bin(int(raw[3])).lstrip('0b').zfill(8)
    integer = int(binnum,2)
    return integer

def findchr(str,chr):
    length = len(str)
    for index in range(length):
        if str[index]==chr:
            return index
    return ERROR

def rfindchr(str,chr):
    length = len(str)
    for index in range(-1,-length,-1):
        if str[index]==chr:
            return length+index
    return ERROR

def subfindchr(str,originchr,newchr):
    index = findchr(str,originchr)
    str = str[0:index]+newchr+str[index+1:]
    return str

def atoc(str):
    length = len(str)
    for i in range(-1,-length,-1):
        if str[i]=='+' or str[i]=='-':
            op1 = str[:i+length]
            op2 = str[i+length:-1]
            break
    print op1,' ',op2
    return complex(float(op1),float(op2))

def Rochambeau():
    while True:
        print """请输入选项：
            1 布
            2 石头
            3 剪子
            4 退出"""
        while True:
            player = raw_input()
            if player not in '1234':
                print '选项不正确，重新输入'
            else:
                break
        player = int(player)
        if player==4:
            break
        robot = random.choice([1,2,3])
        print 'versus ',robot
        rules1 = {1:'E',2:'P',3:'R'}
        rules2 = {1:'R',2:'E',3:'P'}
        rules3 = {1:'P',2:'R',3:'E'}
        rules = {1:rules1,2:rules2,3:rules3}
        score = rules[player][robot]
        res = {'P':'你赢啦','R':'你输啦','E':'平局'}
        print res[score]

# 以下三个函数
# 6-16
def matrixSum():
    print "要进行矩阵加法，行列数必须相同"
    M=[]
    N=[]
    res1 = createMat(M,'M')
    res2 = createMat(N,'N')
    print M
    print N
    row_m = res1[0]
    column_m = res1[1]
    row_n = res2[0]
    column_n = res2[1]
    if row_n!=row_m or column_n!=column_m:
        print '行列数不相等！'
        return ERROR
    row = row_m
    column = column_m
    sumres = copy.copy(M)
    for i in range(row):
        for j in range(column):
            sumres[i][j] = M[i][j]+N[i][j]
    print 'M+N = '
    print sumres
    return None

def matriixMultiply():
    print "要进行矩阵乘法，M的列数必须与N的行数相同"
    M=[]
    N=[]
    res1 = createMat(M,'M')
    res2 = createMat(N,'N')
    row_m = res1[0]
    row_n = res2[0]
    column_m = res1[1]
    column_n = res2[1]
    if column_m != row_n:
        print 'M的列数与N的行数不相等！'
        return ERROR
    print 'M：',M
    print 'N：',N
    multiplyres = []
    for i in range(row_m):
        rowlist = [0]*column_n
        multiplyres.append(rowlist)
    for m in range(column_n):
        for i in range(row_m):
            for j in range(column_m):
                multiplyres[i][m] += M[i][j]*N[j][m]        #很关键 multiplyres的行数=row_m，列数=column_n，column_n有可能大于row_m
    print 'M*N = '
    print multiplyres
    return None

def createMat(mat,name):
    print '输入%s的行数和列数' % name
    row,column = raw_input('行数：'),raw_input('列数：')
    row = int(row)
    column = int(column)
    for i in range(row):
        rowlist = []
        for j in range(column):
            print '输入%s矩阵第%d行第%d个数' % (name,i+1,j+1)
            rowlist.append(int(raw_input()))
        mat.append(rowlist)
    return row,column
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 6-8
# 88 --> eithy-nine
# 输入int数字在0～1000以内
choice1 = ['','one','two','three','four','five','six','seven','eight','nine']
choice2 = ['ten','eleven','tweleve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
choice3 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def numTranslate(num):
    if num<=0 or num>=1000:
        print '输入错误，请重试'
        return ERROR
    if num>0 and num<=99:
        return numTranslate2(num)
    else:
        '三位数'
        res1 = divmod(num,100)
        hundred = res1[0]
        return choice1[hundred]+'hundred-'+numTranslate2(res1[1])

def numTranslate2(num2):
    if num2==0:
        return ''
    if 0 < num2 <= 9:
        '一位数'
        return choice1[num2]
    elif num2>=10 and num2<20:
        '两位数'
        single = num2%10
        return choice2[single]
    elif num2 >= 20 and num2 <= 99:
        '两位数'
        res1 = divmod(num2, 10)
        ten = res1[0]
        single = res1[1]
        return choice3[ten]+'-' + choice1[single]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mutiColumnPrint(alist):
    print """
    用户选项
    1 水平排序
    2 垂直排序
    """
    sortBy = raw_input()
    print """
    请输入列数
    """
    column_count = int(raw_input())
    length = len(alist)
    res = divmod(length,column_count)
    per_column = res[0]
    extra = res[1]                      # 从最后一列开始依次分配给每一列，这个数一定小于列数column_count


    ##水平排序
    # for i in range(length):
    #     for j in range(column_count):
    #         print alist[j] +' ',
    #     print ' '
    print alist
    print per_column
    print column_count
    print length
    ##垂直排序

    n = 0
    for i in range(0, per_column + 1):
        if i == per_column:
            for j in range(0, extra):
                print 4 * column_count * ' ' + str(alist[i * column_count + j])
        else:
            for j in range(0, column_count):
                print "%4s" % str(alist[i + j * per_column]),
            print
        n += 1
        if n % column_count == 0:
            continue








# main function
if __name__ == '__main__':
    pass
