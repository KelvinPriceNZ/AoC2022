#!/usr/bin/env python3

file=list()

with open("./input.txt", "r") as f:
	file=f.read().splitlines()

elves=list()

elf=0
elves.append(0)

for line in file:
	if len(line) > 0:
		elves[elf] += int(line)
	else:
		elf+=1
		elves.append(0)

print(sorted(elves)[-1])
