#!/usr/bin/env python
# encoding:utf-8
import os
import fire
from fire_sun import *
from libs.util import _init, _get_value, _set_value

_init()
_set_value("main_path", os.path.dirname(os.path.realpath(__file__)))


class Main(object):
	def __init__(self):
		self.cpu = Cpu()
		self.memory = Memory()
		self.log = Log()
		self.hba = HBACard()
		self.raid = RaidCard()


if __name__ == '__main__':
	fire.Fire(Main)


