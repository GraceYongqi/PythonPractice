#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : main.py
@Author: Grace
@Date  : 2018/7/12
@Desc  : 实现修改文件内容，使用curse模块，待完成
'''

# import modules
import curses

# global variables
stdscr = curses.initscr()

# class definition


# function definition
def modifyLine():
    lines = []
    print '输入您需要修改的文件名：'
    filename = raw_input()
    print '文件内容如下：'
    try:
        fp = open(filename,'r')
    except IOError, e:
        print "* * * file open error:" ,e
    count = 0
    for eachline in fp:
        print eachline,
        lines.append(eachline)
        count+=1
    fp.close()
    while True:
        print '文件一共%d行, 您需要修改第几行：' % count
        linenum = (int)(raw_input())
        if linenum<1 or linenum>count:
            print '* * * line num error'
        else:
            break
    print '输入指定行的新内容：'
    fp = open(filename , 'w')
    lines[linenum-1] = raw_input()+'\n'
    s = ''.join(lines)
    fp.write(s)
    fp.close()

def set_win():
    pass

def display_info(str, x, y, ):
    pass

def modifyFile():
    pass

# main function
if __name__ == '__main__':
    modifyLine()
#    modifyFile()
