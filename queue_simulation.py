#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : queue_simulation.py
@Author: Grace
@Date  : 2018/8/1
@Desc  : 
'''

# import modules

# global variables
queue = []

def enterQueue():
    '允许多个元素连续进入，以#结束'
    element = raw_input()
    while element is not '#':
        queue.append(element)
        element = raw_input()

def departQueue():
    if len(queue) == 0:
        print '队列为空！'
        return
    delelement = queue.pop(0)
    print 'Removed %s' % delelement
    print 'Now queue is:'
    viewQueue()

def viewQueue():
    for i in queue:
        print i

CMDs = {'e':enterQueue, 'd':departQueue, 'v':viewQueue}

# function definition
def simulateQueue():
    while True:
        ill = """
        Enter
        Depart
        View
        Quit
        Enter your choice:"""
        while True:
            choice = raw_input(ill).strip().lower()
            if choice not in 'edvq':
                print 'Invalid choice, please try again'
            else:
                break
        print 'You chose %s !' % choice
        if choice =='q':
            break
        CMDs[choice]()

# main function
if __name__ == '__main__':
    pass
