#!/usr/bin/env python3

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

X = 1
history = list()
history.append(X)

cycle = 0

for line in lines:
   if line[0:4] == "noop":
      cycle += 1
      history.append(X)

   if line[0:4] == "addx":
      _, amount = line.split()
      history.append(X)
      cycle += 1
      history.append(X)
      X += int(amount)
      cycle += 1

total = 0

for c, value in enumerate(history):
   if c % 20 == 0 and (c/20) % 2 == 1:
      strength = c * value
      total += strength

print(total)
