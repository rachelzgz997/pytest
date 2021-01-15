#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
import yaml
from python_co.python_code import Calculator
import os

yaml_file_path = os.path.dirname(__file__) + "/data/cacl.yml"
@pytest.fixture(scope="session")
def connect():
    print("链接数据库")
    yield
    print("断开数据库")
@pytest.fixture(scope="class")
def get_calc():
    print("获取计算机实例")
    calc = Calculator()
    return calc

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

@pytest.fixture(params=add_datas,ids=myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里的测试数据:{data}")
    yield data
    print("结束")