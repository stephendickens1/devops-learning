#!/bin/bash

directory=/nonsense

if [ -d $directory ]
then
	result=$?
	echo "The directory $directory exists."
else
	result=$?
	echo "The directory $directory doesn't exist."
fi

echo "The exit code for this script run is $result"
