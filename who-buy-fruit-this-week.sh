#! /bin/bash
#author:Jolin Huang
#从A-J之间随即抽取一位同学买水果，根据每个同学的系数不同，命中的概率也不同。

declare -A buyers
buyers=([A]=10 [B]=30 [C]=10 [D]=20 [E]=10 [F]=10 [G]=10 [H]=10 [I]=10 [J]=10)
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
