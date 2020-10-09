import os
import subprocess
import time
from threading import Timer

class Scanner:

		def __init__(self):
			self.bt = {}
			self.ble = {}


		def scanBT(self):
			bt = os.popen('hcitool scan').read()
			for device in bt.split('\n'):
				if '\t' in device:
					split = device.split('\t')
					self.bt[split[1]] = split[2]

		def scanBLE(self):
			ble = os.popen('timeout -s INT 5 hcitool lescan').read()
			devices = ble[ble.index('\n'):].split('\n')
			devices.pop(0)
			devices.pop(-1)
			for device in devices:
				split = device[:device.index(' ')], device[device.index(' ')+1:]
				self.ble[split[0]] = split[1]


#sc = Scanner()
#sc.scanBT()
#print(sc.bt)
#sc.scanBLE()
#print(sc.ble)