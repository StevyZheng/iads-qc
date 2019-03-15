# !/usr/bin/env python
# encoding:utf-8
from libs.hw_op.main_hw import CpuMem
from libs.hw_op.hw_log import LogFile
from libs.err_msg import log_file_list
from libs.sys import *
import json


class Cpu(object):
	def __init__(self):
		pass
	
	def burn(self, burn_core=-1):
		CpuMem.burn_cpu_mem(burn_core)


class Memory(object):
	def __init__(self):
		pass
	
	def burn(self, burn_core=-1):
		CpuMem.burn_cpu_mem(burn_core)


class HBACard(object):
	def __init__(self):
		pass
	
	def info(self):
		ret_dict = Sys.get_hba_info()
		if ret_dict is None:
			raise Exception("System has no hba card!")
		else:
			ret_json_str = json.dumps(ret_dict, indent=2)
			print(ret_json_str)


class RaidCard(object):
	def __init__(self):
		pass
	
	def info(self):
		ret_dict = Sys.get_hwraid_info()
		if ret_dict is None:
			raise Exception("System has no raid card!")
		else:
			ret_json_str = json.dumps(ret_dict, indent=2)
			print(ret_json_str)


class Log(object):
	def __init__(self):
		pass
	
	def analysis(self):
		ret_dict = None
		log_file_messages = LogFile()
		log_file_mcelog = LogFile()
		log_file_messages.set_file(log_file_list[0])
		log_file_messages.load_log()
		err_messages = log_file_messages.scan_log()
		del log_file_messages
		log_file_mcelog.set_file(log_file_list[1])
		log_file_mcelog.load_log()
		err_mcelog = log_file_mcelog.scan_log()
		del log_file_mcelog
		if err_messages is not None and err_mcelog is not None > 0:
			ret_dict = {
				"err_messages": err_messages,
				"err_mcelog": err_mcelog
			}
		elif err_messages is None and err_mcelog is not None:
			ret_dict = {
				"err_mcelog": err_mcelog
			}
		elif err_mcelog is None and err_messages is not None:
			ret_dict = {
				"err_messages": err_messages
			}
		if ret_dict is not None:
			print(json.dumps(ret_dict, indent=2))
		else:
			print("No errors.")


			
		


