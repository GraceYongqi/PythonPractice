#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : userManage.py
@Author: Grace
@Date  : 2018/8/6
@Desc  : 7-5 用户管理（包括注册、登陆、时间戳、密码认证、GUI界面、管理员账户） P187
'''

# import modules
import generalTool
import time
import string
import random
import crypt
from Tkinter import *

# global variables

# class definition

# function definition
warningStr = generalTool.warningStr
adminWelcome = generalTool.adminWelcome

users = {}
interval = 60*60
chars = string.digits + string.letters


def adminSurface():
    print adminWelcome
    while True:
        print """
        (1) Delete one user
        (2) View all users
        (3) Quit"""
        while True:
            command = raw_input()
            if command not in '123':
                print warningStr+'Try again!'
                continue
            else:
                break
        if command =='1':
            usr = raw_input('enter the username:')
            del users[usr.lower()]
            print warningStr+'Delete success!'
        elif command == '2':
            for i in users:
                ltime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(users[i][1])))
                print i,'\t',users[i][0],ltime
        else:
            break

def getSalt():
    '为crypt函数提供盐值，即加密干扰，如不提供将会自动生成一个'
    return random.choice(chars)+random.choice(chars)

def newUser():
    while True:
        nname = raw_input('enter username:').lower()
        if nname in users:
            print warningStr+'Username has existed! Try again!'
        else:
            pass
        flag = 0
        for i in nname:
            if i not in chars:
                print warningStr+'Username doesn\'t contain space or *!'
                flag =1
                break
        if flag==0:
            break
    while True:
        npwd = raw_input('enter passwd:')
        salt = getSalt()
        npwd_crypt = crypt.crypt(npwd,salt)
        re_npwd = raw_input('enter passwd again:')
        re_npwd_crypt = crypt.crypt(re_npwd,salt)
        if re_npwd_crypt==npwd_crypt:
            users.update({nname:[npwd,0.0]})
            print warningStr+'New user has created!'
            break
        else:
            print 'password wrong!'


def oldUser():
    username = raw_input('enter your username:').lower()
    if username not in users:
        print warningStr+'This user not exist! New user?'
        c = raw_input()
        if c.strip().lower()=='y':
            newUser()
            print warningStr+'Now login again'
            oldUser()
        else:
            oldUser()
    else:
        while True:
            password = raw_input('enter your password:')
            if password != users[username][0]:
                print warningStr+'Password wrong!'
                continue
            last_logintime = users[username][1]
            logintime = time.time()
            if logintime - last_logintime < float(interval) and last_logintime!=0:
                print warningStr,'You already logged in at: ',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(last_logintime)))
            else:
                users[username][1] = logintime
                print warningStr+'Login success!'
            break
        if username == 'root':
            adminSurface()
        else:
            pass

def userManagement():
    while True:
        print"""
        New user
        Old user
        Quit"""
        command = raw_input().strip().lower()
        if command not in 'noq':
            print 'try again!'
            continue
        elif command== 'q':
            break
        elif command== 'n':
            newUser()
        elif command== 'o':
            oldUser()

def GUImanagement():
    root = Tk()

# main function
if __name__ == '__main__':
    pass
