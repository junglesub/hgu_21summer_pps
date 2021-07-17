#!/bin/bash
read -p "Day NO: " dayN
read -p "Start End: " start end

for i in $(eval echo "{$start..$end}")
do
  touch "${dayN}-${i}_유정섭_$(date '+%Y%m%d').py"
done