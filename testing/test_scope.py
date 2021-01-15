#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
# function 每一条测试用例前后都会执行一次fixture
# class 这个类前后都会执行一次fixture
# module 整个测试用例执行前后就执行一次fixture


class TestDemo:
    def test_a(self,connect):
        print("测试用例1")
    def test_b(self,connect):
        print("测试用例2")

class TestDemo1:
    def test_c(self,connect):
        print("测试用例3")
    def test_d(self,connect):
        print("测试用例4")