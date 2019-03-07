# !/usr/bin/env python
# encoding:utf-8
import os
import datetime
import sys
import psutil
import time
import subprocess
from libs.util import TextOp


def get_now_time():
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


class Sys:
    def __init__(self):
        pass

    @staticmethod
    def shell_exec_single(cmdstring, timeout=8):
        """
        :param cmdstring: str, shell command
        :param timeout: int
        :return: str, execute result
        """
        if timeout:
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
        sub = subprocess.Popen(cmdstring, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while True:
            if sub.poll() is not None:
                break
            time.sleep(0.1)
            if timeout:
                if end_time <= datetime.datetime.now():
                    sub.kill()
                    return "TIME_OUT"
        return str(sub.stdout.read())

    @staticmethod
    def get_time():
        return get_now_time()

    @staticmethod
    def get_mem_info():
        """
        :rtype: vector (total memsize, free memsize), MB
        """
        memory_convent = 1024 * 1024
        mem = psutil.virtual_memory()
        return mem.total / memory_convent, mem.total / memory_convent - mem.used / (1024 * 1024)

    @staticmethod
    def get_cpu_info():
        """
        :return: dict {socket_num, cpu_num, cpu_model, cpu_core, cpu_stepping}
        """
        dmi_str = Sys.shell_exec_single("dmidecode -t processor")
        t_list_socket = TextOp.find_str(dmi_str, ".+Socket Designation.+", False)
        t_list_cpu_model = TextOp.find_str_column(dmi_str, ".+Version:.+", 1, ":", False)
        t_list_cpu_core = TextOp.find_str_column(dmi_str, ".+Core Count:.+", 1, ":", False)
        t_list_cpu_stepping = TextOp.find_str_column(dmi_str, "Stepping [0-9]+", 1, " ", False)
        if t_list_socket is None:
            return {}
        ret_dict = {
            "socket_num": t_list_socket.count(),
            "cpu_num": t_list_cpu_model.count(),
            "cpu_model": str(t_list_cpu_model[0]).strip(),
            "cpu_core": int(str(t_list_cpu_core[0]).strip()),
            "cpu_stepping": str(t_list_cpu_stepping[0]).strip()
        }
        return ret_dict



