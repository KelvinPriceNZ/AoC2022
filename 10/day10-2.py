#!/usr/bin/env python3
import math

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

X = 1

cycle = 0
print("█", end="")

def tick():
   global X
   global cycle

   cycle += 1

   pixel = cycle % 40

   pixel_on = abs(X - pixel) < 2 

   print("█" if pixel_on else " ", end="")

   if pixel == 39 : print()

for line in lines:
   tick()

   instr = line[0:4]

   if instr == "noop":
      pass
   elif instr == "addx":
      amount = int(line[5:])
      X += amount

      tick()
