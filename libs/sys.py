# !/usr/bin/env python
# encoding:utf-8
import os

import datetime

import sys
import psutil
import time
import subprocess


def get_now_time():
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


class Sys:
    def __init__(self):
        pass

    @staticmethod
    def shell_exec_single(cmdstring, timeout=None):
        """
        :param cmdstring: str, shell command
        :param timeout: int
        :return: str, execute result
        """
        if timeout:
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
        sub = subprocess.Popen(cmdstring, stdin=subprocess.PIPE, bufsize=4096, shell=True)
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
        :return: dict {socket_num, cpu_num, cpu_model, cpu_core, cpu_step}
        """

        pass



