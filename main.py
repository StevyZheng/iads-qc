# !/usr/bin/env python
# encoding:utf-8
import fire
from fire_sun import *


class Main(object):
    def __init__(self):
        self.cpu = Cpu()
        self.memory = Memory()
        self.log = Log()


if __name__ == '__main__':
    fire.Fire(Main)


