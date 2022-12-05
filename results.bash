#!/bin/bash

for day in {01..25}
do
   cd $day

   echo -n "Day $(basename $day)"

   for part in 1 2
   do
      soln="./day${day}-${part}.py"
      echo -en "\tPart $part"
      if [ -s ${soln} ]
      then
         echo -en "\t\t"
         $soln
      else
         echo -e "\t\t*Unsolved*"
      fi
   done
   cd ~-
done
