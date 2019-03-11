# !/usr/bin/env python
# encoding:utf-8

log_file_list = ["/var/log/messages", "/var/log/mcelog"]

linux_err_msg = {
	"Call Trace": "linux kernel error.",
	"No space left on device": "disk No space left on device",
	"Medium Error": "disk is broken.",
	"I/O error": "disk sector error or the signal between the disk and the disk controller is unstable.",
	"Device offlined": "Device offlined",
	"I/O error, dev": "disk or controler is broken or missing.",
}
