#!/usr/bin/env python3
import math

symbol = {
   True:  "█",
   False: " "
}

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

X = 1

cycle = 0

def tick():
   global X
   global cycle

   pixel = cycle % 40

   pixel_on = abs(pixel - X) < 2

   print(f"{symbol[pixel_on]}", end="")

   if pixel == 39 : print()

   cycle += 1

for line in lines:
   tick()

   instr = line[0:4]

   if instr == "noop":
      pass
   elif instr == "addx":
      tick()

      amount = int(line[5:])
      X += amount
