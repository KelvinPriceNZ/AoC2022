#!/usr/bin/env python3

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

move = False
stacks = list()

for line in lines:
   if len(line) == 0:
      move = True
      continue

   if not move:
      s = 0
      for p in range(1,len(line)+1, 4):
         if len(stacks) <= s:
            stacks.append(list())
         if line[p].isalpha():
            stacks[s].insert(0,line[p])
         s+=1
   else:
      instructions = line.split()
      count = int(instructions[1])
      s_from = int(instructions[3]) - 1
      s_to = int(instructions[5]) - 1

      for m in range(count):
         t = stacks[s_from].pop()
         stacks[s_to].append(t)

for s in range(len(stacks)):
   print(stacks[s].pop(), end='')

print()
