#!/bin/bash

mynum=300
exists="The file exists"
deleting="Deleting the file"

notexist="The file does not exist"
creating="Creating the file"

loop_count=3

if [ -f ~/myfile.sh ]
then
	for ((i = 0; i < loop_count; i++)); do

		echo -ne "$exists.\r"
		sleep 0.5
		echo -ne "$exists..\r"
		sleep 0.5
		echo -ne "$exists...\r"
		sleep 0.5
		echo -ne "$exists   \r"
		sleep 0.5
	done

	echo "$exists..."
	for ((i = 0; i < loop_count; i++)); do
		echo -ne "$deleting.\r"
                sleep 0.5
                echo -ne "$deleting..\r"
                sleep 0.5
                echo -ne "$deleting...\r"
                sleep 0.5
                echo -ne "$deleting   \r"
                sleep 0.5
        done

	echo "$deleting..."
	rm ~/myfile.sh
	echo -e "\e[5mI killed the file!\e[25m"
else
	for ((i = 0; i < loop_count; i++)); do

                echo -ne "$notexist.\r"
                sleep 0.5
                echo -ne "$notexist..\r"
                sleep 0.5
                echo -ne "$notexist...\r"
                sleep 0.5
                echo -ne "$notexist   \r"
                sleep 0.5
        done

        echo "$notexist..."
        for ((i = 0; i < loop_count; i++)); do
                echo -ne "$creating.\r"
                sleep 0.5
                echo -ne "$creating..\r"
                sleep 0.5
                echo -ne "$creating...\r"
                sleep 0.5
                echo -ne "$creating   \r"
                sleep 0.5
        done

        echo "$creating..."
        touch ~/myfile.sh
        echo -e "\e[5mI made the file!\e[25m"
fi
