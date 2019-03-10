# !/usr/bin/env python
# encoding:utf-8
import inspect
import os
import re
import traceback
import numpy as np


class Debug(object):
    """  调试及异常相关函数方法 """
    def __init__(self):
        pass

    @classmethod
    def get_class(cls, dist_cls):
        """
        :param dist_cls: 目标类
        :return: 返回调用函数的类名
        """
        return dist_cls.__name__

    @classmethod
    def get_class_mod(cls, dist_cls):
        """
        :param dist_cls: 目标类
        :return: 返回目标类中调用函数的模块全名
        """
        return dist_cls.__module__

    @classmethod
    def get_current_function_name(cls):
        """
        :return: 返回当前的函数名
        """
        return inspect.stack()[1][3]

    @classmethod
    def get_except(cls, ex):
        """
        :param ex: 异常变量
        :return: 返回要打印的异常字符串
        """
        return "exception msg:{0}{1}{0}traceback:{0}{2}".format(os.linesep, Exception(ex).message, traceback.format_exc())


class TextOp(object):
    def __init__(self):
        pass

    @classmethod
    def find_str(cls, src_str, reg_str, case=True, strip=True):
        """
        :param strip:
        :param src_str:
        :param reg_str:
        :param case: true upper lower, false not
        :return: list
        """
        if case:
            it = re.finditer(reg_str, src_str)
        else:
            it = re.finditer(reg_str, src_str, re.I)
        ret_list = []
        for match in it:
            if match is not None:
                if strip:
                    ret_str = match.group().strip()
                else:
                    ret_str = match.group()
                ret_list.append(ret_str)
        return ret_list
    
    @classmethod
    def find_str_column(cls, src_str, reg_str, column, split_str, case=True, strip=True):
        """
        :param strip:
        :param src_str:
        :param reg_str:
        :param column: 列号
        :param split_str: 化分列的字符串
        :param case: true upper lower, false not
        :return: list
        """
        row_list = TextOp.find_str(src_str, reg_str, case, strip)
        ret_list = []
        for row_str in row_list:
            split_list = row_str.split(split_str)
            if len(split_list) > column:
                ret_list.append(split_list[column])
        return ret_list


class Math(object):
    def __init__(self):
        pass
    
    @classmethod
    def solve_equations(cls):
        """
        CPU、内存负载，单进程占一个线程，占1GB内存
        :return: 求得的方程解
        """
        matrix_a = np.random.rand(8000, 8000)
        matrix_b = np.random.rand(8000, 1)
        matrix_ret = np.linalg.solve(matrix_a, matrix_b)
        print(matrix_ret)
        



