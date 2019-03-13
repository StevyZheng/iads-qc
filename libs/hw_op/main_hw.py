# !/usr/bin/env python
# encoding:utf-8
from multiprocessing import pool as mp
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
        mem_size_GB = int(mem_size / 1024)
        if cpu_core_num >= burn_core_count >= 0:
            cpu_core_num = burn_core_count
        if mem_size_GB < cpu_core_num * 2:
            cpu_core_num = mem_size_GB / 2
        if cpu_core_num > 0:
            cpu_core_num = cpu_core_num * 2 - 1
            p = mp.Pool(processes=cpu_core_num)
            for th in range(cpu_core_num):
                p.apply_async(Math.solve_equations)
            p.close()
            p.join()
        else:
            raise Exception("error: cpu_core_num <= 0!")

            

