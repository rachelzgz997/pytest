#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest


@pytest.fixture(params=[1,2,3])
def login1(request):
    data = request.param
    print("测试数据")
    return data

def test_case1(login1):
    print(login1)
    print("测试用例1")
