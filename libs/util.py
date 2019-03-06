# !/usr/bin/env python
# encoding:utf-8

import os
import re


class TextOp:
    def __init__(self):
        pass

    @staticmethod
    def find_str(src_str, reg_str, case=True):
        """
        :param src_str:
        :param reg_str:
        :param case: true upper lower, false not
        :return: list
        """
        if case:
            ret_list = re.findall(reg_str, src_str)
        else:
            ret_list = re.findall(reg_str, src_str, re.I)
        return ret_list
