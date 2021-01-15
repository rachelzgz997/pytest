#!/usr/bin/python
# -*- coding:utf-8 -*-

def provider():
    for i in range(1,10):
        print("这是开始")
        #相当于return i
        yield i
        print("这是结束")
p = provider()
for i in p:
    print(next(p))