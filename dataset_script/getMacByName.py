import os
import subprocess
import time
import pexpect

def scanBLE():
	ble_devices = {}
	ble = os.popen('timeout -s INT 5 hcitool lescan').read()
	devices = ble[ble.index('\n'):].split('\n')
	devices.pop(0)
	devices.pop(-1)
	for device in devices:
		split = device[:device.index(' ')], device[device.index(' ')+1:]
		ble_devices[split[0]] = split[1]

	return ble_devices

def selectDevice(devices, name):
	mac = None
	for device in devices:
		if name == devices[device]:
			mac = device
	return mac


devices = scanBLE()
device = selectDevice(devices, 'Adri_ESP32')
print(device)

gatttool = pexpect.spawn(f"gatttool -i hci0 -b {device} -I")
gatttool.sendline("connect")

gatttool.expect("Connection successful", timeout=3)

gatttool.sendline('char-desc')
gatttool.sendline('exit')


