#!/usr/bin/env python3
import math

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

X = 1
history = [ X ]

cycle = 0
print("█", end="")

def tick():
   global X
   global cycle
   global history

   cycle += 1
   history.append(X)

   pos = cycle % 40

   if abs(X - pos) < 2:
      print("█", end="")
   else:
      print(" ", end="")

   if pos == 39 : print()

for line in lines:
   tick()

   instr = line[0:4]

   if instr == "noop":
      pass
   elif instr == "addx":
      amount = int(line[5:])
      X += amount

      tick()
