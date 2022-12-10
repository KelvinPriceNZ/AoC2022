#!/bin/bash

for day in {01..25}
do
   cd $day

   for part in 1 2
   do
      soln="./day${day}-${part}.py"
      echo -e "Day $(basename $day) Part $part"
      if [ -s ${soln} ]
      then
         $soln
      else
         echo -e "*Unsolved*"
      fi
   done
   cd ~-
done
