# !/usr/bin/env python
# encoding:utf-8
from libs.sys import Sys
from libs.util import TextOp


with open("x.txt") as fp:
    txt = fp.read()
print(TextOp.find_str(txt, ".+Version.+"))


