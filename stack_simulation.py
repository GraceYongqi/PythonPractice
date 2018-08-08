#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : stack_simulation.py
@Author: Grace
@Date  : 2018/8/1
@Desc  : 用列表的数据结构分别模拟栈和队列
'''

# import modules
import copy
# global variables
stack = []

def pushit():
    '允许连续push多个元素进栈'
    print '请输入元素，以#结束'
    element = raw_input()
    while  element is not '#':
        stack.append(element)
        element = raw_input()


def popit():
    if len(stack)==0:
        print '栈为空！'
        return
    else:
        delelement = stack.pop()
        print 'Removed \'%s\' ' % delelement
        print 'Now stack is:'
        viewstack()

def viewstack():
#    stackview = stack
    stackview = copy.copy(stack)
    stackview.reverse()
    for i in stackview:
        print i

CMDs = {'u':pushit, 'o':popit, 'v':viewstack}

# function definition
def simulateStack():
    while True:
        ill = """
        pUsh
        pOp
        View
        Quit
        Enter your choice:"""
        while True:
            choice = raw_input(ill).strip().lower()
            if choice not in 'uovq':
                print 'Invalid choice, please try again!'
            else:
                break
        print 'you chose %s ' % choice
        if choice =='q':
            break
        CMDs[choice]()

# main function
if __name__ == '__main__':
    pass
