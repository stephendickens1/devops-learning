#!/bin/bash

myvar=1

touch ./testfile

while [ -f ./testfile ]
do
	echo "The test file exists as of $(date)."
sleep 1
done

echo "The file no longer exists. It was deleted on $(date)."
