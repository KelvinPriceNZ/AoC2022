#!/usr/bin/env python3
import math

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

X = 1
history = list()
history.append(X)

cycle = 0
print("#", end="")

for line in lines:
   if line[0:4] == "noop":
      cycle += 1
      pos = cycle % 40
      if pos == 0 : print()
      history.append(X)
      if abs(X - pos) < 2:
         print("#", end="")
      else:
         print(".", end="")

   if line[0:4] == "addx":
      _, amount = line.split()
      history.append(X)
      cycle += 1
      pos = cycle % 40
      if pos == 0 : print()
      if abs(X - pos) < 2:
         print("#", end="")
      else:
         print(".", end="")
      history.append(X)
      X += int(amount)
      cycle += 1
      pos = cycle % 40
      if pos == 0 : print()
      if abs(X - pos) < 2:
         print("#", end="")
      else:
         print(".", end="")
