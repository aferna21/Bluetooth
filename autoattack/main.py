import scanner

def scanMenu():
	print("\nWelcome. Choose an option: ")
	print("Press 0 to exit")
	print("Press 1 to scan BT")
	print("Press 2 to scan BLE")
	print("Press 3 to see all devices")
	print("Press 4 to see BT devices")
	print("Press 5 to see BLE devices")
	print("Press 6 to attack")


def attackMenu():
	print("\nAttack menu. Choose an option: ")
	print("Press 0 to return to Scan Menu")
	print("Press 1 to auth in device")

def printDevices(version, devices):
	print(f"************\nThe {version} devices are: ")
	for device in devices:
		print(f"MAC-> {device}\t Name-> {devices[device]}")
	print("************")

def selectDevice(version, devices):
	print("************")
	print(f"Select a {version} device: ")
	dev_selected = -1
	i=0
	for device in devices:
		i+=1
		print(f"Press {i} to select {device}, {devices[device]}")
	print("************")
	dev_selected = int(input())
	mac = list(devices)[dev_selected-1]
	return {mac, devices[mac]}

def scanBT():
	sc = scanner.Scanner()
	sc.scanBT()
	return sc.bt

def scanBLE():
	sc = scanner.Scanner()
	sc.scanBLE()
	return sc.ble







###################################### MAIN ###################################### 
scan_opcion = -1
attack_opcion = -1
attack = False
devices_bt = {}
devices_ble = {}

while scan_opcion != 0:

	if(not attack):
		scanMenu()

		scan_opcion = int(input())

		if scan_opcion == 1:
			devices_bt = scanBT()
		
		elif scan_opcion == 2:
			devices_ble = scanBLE()

		elif scan_opcion == 3:
			printDevices("BT", devices_bt)
			printDevices("BLE", devices_ble)

		elif scan_opcion == 4:
			printDevices("BT", devices_bt)

		elif scan_opcion == 5:
			printDevices("BLE", devices_ble)

		elif scan_opcion == 6:
			attack = True

	
	else:
		attackMenu()

		attack_opcion = int(input())

		if attack_opcion == 0:
			attack = False

		elif attack_opcion == 1:
			print(selectDevice("BT", devices_ble))