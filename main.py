# !/usr/bin/env python
# encoding:utf-8
import fire
from fire_sun import *
from libs.util import Math


class Main(object):
    def __init__(self):
        self.cpu = Cpu()
        self.memory = Memory()
    
    def test(self):
        Math.solve_equations()


if __name__ == '__main__':
    fire.Fire(Main)


