#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Author  : Stevy
import re
from libs.util import Debug
from libs.err_msg import linux_err_msg


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

	def scan_log(self):
		ret_flag = False
		ret_dict = {}
		if self.log_str != "":
			for err_it in linux_err_msg:
				it = re.finditer(".*{0}.*".format(err_it), self.log_str, re.I)
				for match in it:
					if match is not None:
						ret_flag = True
						ret_str = match.group().strip()
						ret_dict[ret_str] = linux_err_msg[err_it]
		if ret_flag:
			return ret_dict
		else:
			return None
	

class HwInfo(object):
	def __init__(self):
		self.collect_files = ["/var/log", "/proc", "/var/crash"]
	




