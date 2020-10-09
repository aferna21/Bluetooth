#!/bin/bash


sleep_() {
	rand_to_sleep=$(( $RANDOM % 5 + 2 ))
	echo "Sleeping for $rand_to_sleep seconds..."
	sleep $rand_to_sleep
}


mac=$(python3 getMacByName.py)

if [ "$mac" = "None" ]; then
	echo "Device not found."
	exit
else
	values=(686579 486f6c61204d756e646f2121203a29 4c6f72656d20697073756d206574630a)
	#echo ${values[@]}
	length=${#values[@]}
	for i in {1..500}
	do
		random=$(($RANDOM % $length))
		value=${values[$random]}
		value_ascii=$(echo $value | xxd -r -p)
		gatttool -i hci0 -b $mac --char-write-req -a 0x002a -n $value
		#echo $value

		timestamp=$(date +'%s')
		log="Timestamp: ${timestamp} Value: ${value} (${value_ascii})"
		echo $log >> timestamp.txt

		sleep_ 
	done
	

fi




