# !/usr/bin/env python
# encoding:utf-8
from libs.hardware.main_hw import CpuMem


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
