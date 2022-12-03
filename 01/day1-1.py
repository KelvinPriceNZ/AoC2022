#!/usr/bin/env python3

file=list()

elves=list()

elf=0
elves.append(0)

with open("./input.txt", "r") as f:
   for line in map(str.strip, f):
      if len(line) > 0:
         elves[elf] += int(line)
      else:
         elf+=1
         elves.append(0)

answer = sorted(elves)[-1]

print(answer)
