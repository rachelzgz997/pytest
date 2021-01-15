#!/usr/bin/python
# -*- coding:utf-8 -*-


def test_a(get_calc):
    result = get_calc.add(1,2)
    assert result == 3
