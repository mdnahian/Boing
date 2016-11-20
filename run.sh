#!/bin/bash

IP="192.168.4.156"
FILE="file.wav"
USER="mdislam"
DIR="/Volumes/STORAGE/Python\ Projects/Boing/files/"
#DIR="/Users/mdislam/"


count=1
while true; do
	# ping $IP


	{ scp -r $FILE $USER@$IP:"$DIR"  && 
	echo "[INFO] Copied $count file..." ||
	echo "[ERROR] you fucked up"; } &
	
	mplayer $FILE &> /dev/null &
	{ echo "Recording..." &&
	./speaker.py &> /dev/null; } &

	echo "Flushing..."
	sleep 0.5
	
	wait
	# sleep 5
	
	((count++))
done
