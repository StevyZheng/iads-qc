# !/usr/bin/env python
# encoding:utf-8
import datetime
import psutil
import time
import subprocess
from libs.util import TextOp, Debug


def get_now_time():
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


class Sys(object):
    def __init__(self):
        pass

    @classmethod
    def shell_exec_single(cls, cmdstring, timeout=8):
        """
        :param cmdstring: str, shell command
        :param timeout: int
        :return: str, execute result
        """
        if timeout:
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
        sub = subprocess.Popen(cmdstring, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True)
        while True:
            if sub.poll() is not None:
                break
            time.sleep(0.1)
            if timeout:
                if end_time <= datetime.datetime.now():
                    sub.kill()
                    return "TIME_OUT"
        return str(sub.stdout.read())

    @classmethod
    def get_time(cls):
        return get_now_time()

    @classmethod
    def get_mem_info(cls):
        """
        :return: dict {total memsize, available memsize, free memsize}, MB
        """
        memory_convent = 1024 * 1024
        mem = psutil.virtual_memory()

        dmi_str = Sys.shell_exec_single("dmidecode -t memory")
        t_list_mem_socket = TextOp.find_str(dmi_str, "P[1-9]-DIMM[A-Z]+[1-9]+$", False)
        max_mem_size = TextOp.find_str_column(dmi_str, "Maximum Capacity.+", 1, ":")
        t_list_mem_model = TextOp.find_str(dmi_str, "Part Number.{2}[^D].+", False)
        mem_dict = {}
        try:
            mem_dict = {
                "mem_socet_num": len(t_list_mem_socket),
                "max_mem_size": max_mem_size,
                "mem_model": t_list_mem_model[0],
                "total": mem.total / memory_convent,
                "available": mem.available / memory_convent,
                "free": mem.free / memory_convent
            }
        except Exception as ex:
            print(Debug.get_except(ex))
        return mem_dict

    @classmethod
    def get_cpu_info(cls):
        """
        :return: dict {socket_num, cpu_num, cpu_model, cpu_core, cpu_stepping}
        """
        ret_dict = {}
        dmi_str = Sys.shell_exec_single("dmidecode -t processor")
        t_list_socket = TextOp.find_str(dmi_str, ".+Socket Designation.+", False)
        t_list_cpu_model = TextOp.find_str_column(dmi_str, ".+Version.+", 1, ":", False)
        t_list_cpu_core = TextOp.find_str_column(dmi_str, ".+Core Count:.+", 1, ":", False)
        t_list_cpu_stepping = TextOp.find_str_column(dmi_str, "Stepping [0-9]+", 1, " ", False)
        if t_list_socket is None:
            return {}
        try:
            ret_dict = {
                "socket_num": len(t_list_socket),
                "cpu_num": len(t_list_cpu_model),
                "cpu_model": str(t_list_cpu_model[0]),
                "cpu_core": int(str(t_list_cpu_core[0])),
                "cpu_stepping": str(t_list_cpu_stepping[0])
            }
        except Exception as ex:
            print(Debug.get_except(ex))
        return ret_dict
