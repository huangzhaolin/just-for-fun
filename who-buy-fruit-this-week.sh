#! /bin/bash
declare -A buyers
buyers=([����]=10 [ƽ��]=30 [����]=10 [����]=20 [����]=10 [����]=10 [����]=10 [��ɭ]=10 [���]=10 [����]=10)
selector=""
index=0
sumSelector=0
for buyer in ${!buyers[*]}
do
	buyerCounter=${buyers[$buyer]}
	((sumSelector=$sumSelector+$buyerCounter))
	for i in `seq $buyerCounter`
	do
		selector[((index++))]=$buyer
	done
done
((random=$RANDOM%$sumSelector))
echo ${selector[$random]} 
