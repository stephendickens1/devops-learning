#!/bin/bash

myvar=1
limit=10
count=0

echo "myvar is equal to $myvar! Let's run it through a while loop"
sleep 3
while [ $myvar -le $limit ]
do 
	echo $myvar
	myvar=$(( $myvar +1 ))
	count=$(( $count +1 ))
	sleep 0.1
done

echo "myvar is now equal to $myvar. The loop ran $count times, making myvar greater than $limit so the loop is over!"
