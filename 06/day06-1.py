#!/usr/bin/env python3

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

for line in lines:
   for p, c in enumerate(line[:-4]):
      block=line[p:p+4]
      if len(set(block)) == 4:
         print(p+4)
         break
