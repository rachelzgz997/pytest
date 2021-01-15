#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest


@pytest.fixture(autouse=True)
def login():
    print("登陆操作")
    username = "zhu"
    password = "123456"
    token = "123456"
    yield[username,password,token]
    print("登出操作")
#需要提前登陆
def test_case1(connect):
    print(f"login information:{connect}")
    print("测试用例1")
def test_case2():
    print("测试用例2")
#需要提前登陆
def test_case3(connect):
    print("测试用例3")

@pytest.mark.usefixtures("connect")
def test_case4():
    print("测试用例4")