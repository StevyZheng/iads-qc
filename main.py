# !/usr/bin/env python
# encoding:utf-8
from libs.sys import Sys
from libs.util import TextOp


print(TextOp.find_str("33  123456dfgr 234 \n  654dfw \n1234", ".*df.*", strip=True))
print(TextOp.find_str_column("33  123456dfgr 234 \n  654dfw \n1234", ".*df.*", 1, " ", strip=True))
