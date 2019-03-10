#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Author  : Stevy
from libs.util import Debug


class LogFile(object):
	def __init__(self):
		self.logfp = None
		self.log_str = ""
	
	def set_file(self, log_path):
		if not isinstance(log_path, str):
			raise Exception("error: log_path is not string.")
		try:
			self.logfp = open(log_path, "r")
		except IOError as ex:
			print(Debug.get_except(ex))

	def __del__(self):
		if self.logfp is not None:
			self.logfp.close()
	
	def load_log(self):
		try:
			if self.logfp:
				self.log_str = self.logfp.read()
		except IOError as ex:
			print(Debug.get_except(ex))

	def scan_log(self, call_back_func):
		err_dict = {}
		if call_back_func is not None:
			
			call_back_func(self.log_str)

