#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : test.py
@Author: Grace
@Date  : 2018/7/15
@Desc  : 调用各小节练习题的实现方法
'''

# import modules
import numCaculator
import seqPractice
import stack_simulation
import queue_simulation
# global variables

# class definition

# function definition

# main function
if __name__ == '__main__':
    #第七章
    # print "请输入表达式，支持+ - * ／ **五种运算符："
    # str = raw_input()
    # print '结果为：',numCaculator.CalculateBySplit(str)

    #print numCaculator.conversionRes()

    # print '请输入两个数：'
    # x = int(raw_input())
    # y = int(raw_input())
    # GreatestCommonDivisor = numCaculator.EuclideanAlgorithm(x,y)
    # print '最大公约数为：',GreatestCommonDivisor
    # print '最小公倍数为：',x*y/GreatestCommonDivisor

    #numCaculator.FinanceCalculator()

    #numCaculator.FetchRandom()

    #第六章
    # stack_simulation.simulateStack()
    # queue_simulation.simulateQueue()
    #6-2
    # rawid = raw_input('input a identifier:')
    # res = seqPractice.idChecher(rawid)
    # if res == True:
    #     print 'correct!'
    # else:
    #     print 'wrong!'

    #6-5 (c)
    # res = seqPractice.palindromeJudge(raw_input())
    # if res is True:
    #     print 'correct!'
    # else:
    #     print 'wrong!'

    #6-5 (d)
    seqPractice.palindromeGenerator(raw_input())