# !/usr/bin/env python
# encoding:utf-8

import os
import re


class TextOp:
    def __init__(self):
        pass

    @staticmethod
    def find_str(src_str, reg_str, case=True, strip=True):
        """
        :param strip:
        :param src_str:
        :param reg_str:
        :param case: true upper lower, false not
        :return: list
        """
        if strip:
            reg_str = "\S" + reg_str + "\S"
        if case:
            ret_list = re.findall(reg_str, src_str)
        else:
            ret_list = re.findall(reg_str, src_str, re.I)
        return ret_list
    
    @staticmethod
    def find_str_column(src_str, reg_str, column, split_str, case=True, strip=True):
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
