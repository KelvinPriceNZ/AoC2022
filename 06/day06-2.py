#!/usr/bin/env python3

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

for line in lines:
   for p, c in enumerate(line[:-14]):
      block=line[p:p+14]
      if len(set(block)) == 14:
         print(p+14)
         break
