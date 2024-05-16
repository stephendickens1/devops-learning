#!/bin/bash

bedtime="2310"  # Set bedtime to 00:01 in 24-hour format without the colon

while [ "$(date +%H%M)" -lt "$bedtime" ]
do
    echo "Sleep is for the weak, it's only $(date +%T)!"
    sleep 5
done

echo -e "\e[5mIT'S BED TIME!\e[25m"
