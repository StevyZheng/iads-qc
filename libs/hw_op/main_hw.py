# !/usr/bin/env python
# encoding:utf-8
import multiprocessing
from libs.sys import Sys
from libs.util import Math


class CpuMem(object):
	def __init__(self):
		pass

	@classmethod
	def burn_cpu_mem(cls, burn_core_count=-1):
		"""
		:param burn_core_count: 参加负载的核心数
		:return:
		"""
		cpu_info = Sys.get_cpu_info()
		mem_info = Sys.get_mem_info()
		if cpu_info is None or mem_info is None:
			raise Exception("error: cpu_info is None or mem_info is None.")
		cpu_core_num = mem_size = 0
		if "cpu_core" in cpu_info and "cpu_num" in cpu_info:
			cpu_core_num = cpu_info["cpu_core"] * cpu_info["cpu_num"]
		if "available" in mem_info:
			mem_size = mem_info["available"]
		if cpu_core_num >= burn_core_count >= 0:
			cpu_core_num = burn_core_count
		mem_per_process = 500
		mem_process = mem_size / mem_per_process
		if mem_process > cpu_core_num * 2:
			run_process = mem_process - 1
		else:
			run_process = cpu_core_num * 2 - 1
		if cpu_core_num > 0:
			p_list = []
			for th in range(run_process):
				p = multiprocessing.Process(target=Math.solve_equations)
				p_list.append(p)
			for p1 in p_list:
				p1.start()
			for p1 in p_list:
				p1.join()
		else:
			raise Exception("error: cpu_core_num <= 0!")

			
class Disk(object):
	def __init__(self):
		pass



