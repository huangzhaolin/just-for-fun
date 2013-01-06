#! /bin/bash
declare -A buyers
buyers=([³¯ÁØ]=10 [Æ½ÖÎ]=30 [ÓÄÇÇ]=10 [ÖÁ³Ï]=20 [ËÎÒâ]=10 [±±·å]=10 [ÀëÏã]=10 [¼ªÉ­]=10 [³Ìá°]=10 [ÁÁÁÁ]=10)
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
