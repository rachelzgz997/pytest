import pytest
from python_co.python_code import Calculator
import yaml



class TestCalc:
    def test_add(self,get_calc,get_add_datas):
        result = None
        try:
            #实例化计算器类
            # calc = Calculator()
            #调用add方法
            result = get_calc.add(get_add_datas[0],get_add_datas[1])
            #得到结果之后，需要写断言

            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)

        assert result == get_add_datas[2]
    # def test_add1(self,a,b,expect):
    #     # 实例化计算器类
    #     calc = Calculator()
    #     # 调用add方法
    #     result = calc.add(a,b)
    #     # 得到结果之后，需要写断言
    #     assert result == expect
    #
    # def test_add2(self,a,b,expect):
    #     # 实例化计算器类
    #     calc = Calculator()
    #     # 调用add方法
    #     result = calc.add(a,b)
    #     # 得到结果之后，需要写断言
    #     assert result == expect
