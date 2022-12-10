#!/usr/bin/env python3

cycle = 0
total = 0

X = 1
history = [ X ]

def signal_strength(cycle, X):
   if cycle % 20 == 0 and (cycle/20) % 2 == 1:
      return cycle * X
   else:
      return 0

def tick():
   global cycle
   global history
   global total
   global X

   cycle += 1
   history.append(X)
   total += signal_strength(cycle, X)

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

for line in lines:
   tick()

   instr = line[0:4]

   if line[0:4] == "addx":
      tick()
      amount = int(line[5:])
      X += amount
   elif instr == "noop":
      pass

print(total)
