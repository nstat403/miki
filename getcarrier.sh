#!/bin/sh

#echo $1
#durationtime=$1

read -p "duration time:" durationtime;
duration=$(($durationtime / 1))

#echo $duration
#day=echo $(python ~/storage/shared/Documents/py/getdate.py)

#for i in {1..${duration}};do
for i in $(seq 1 ${duration});do
echo $i
#day=$(echo $(python $HOME/storage/shared/Documents/py/getdate.py))
#carrier=$(termux-telephony-deviceinfo|grep "network_operator_name")
#echo $i $day $carrier >> network.txt
echo $(python $HOME/storage/shared/Documents/py/getnetworkinfo.py) >> network.txt

sleep 60

done

exit 1
