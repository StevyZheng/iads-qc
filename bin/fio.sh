#!/usr/bin/env bash

fio --name=PR_IO_Test --rw=randread --direct=1 --ioengine=libaio