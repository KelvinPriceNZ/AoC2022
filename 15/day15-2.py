#!/usr/bin/env python3
import curses
import math
import re
from collections import deque
import numpy as np
import sys

matcher = re.compile(r"x=([-0-9]+), y=([-0-9]+)")

def mh(d1, d2):
   d1x, d1y = d1
   d2x, d2y = d2

   return abs(d1x - d2x) + abs(d1y - d2y)

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

sensors = list()
beacons = list()
manhattens = list()
borders = list()

min_x = math.inf
max_x = -math.inf

# Example
width = 20
# Real
width = 4_000_000

def get_boundaries(x,y,d):
   b = set()
   for mx in range(x-d,x+d+1):
      if not 0 <= mx <= width : continue

      x_off = abs(mx - x)
      y_off = d - x_off

      for my in [ y + y_off, y - y_off ]:
         if not 0 <= my <= width: continue
         if mh((mx, my),(x,y)) == d:
            b.add((mx,my))

   return b

for line in lines:
   sensor, beacon = line.split(":",2)
   m = matcher.search(sensor)
   sensor_x = int(m.group(1))
   sensor_y = int(m.group(2))
   m = matcher.search(beacon)
   beacon_x = int(m.group(1))
   beacon_y = int(m.group(2))
   beacons.append((beacon_x,beacon_y))
   sensors.append((sensor_x,sensor_y))
   min_x = min([min_x, sensor_x,beacon_x])
   max_x = max([max_x, sensor_x,beacon_x])

   mh_distance = mh((sensor_x,sensor_y),(beacon_x,beacon_y))
   manhattens.append(mh_distance)

   border_list = get_boundaries(sensor_x, sensor_y, mh_distance + 1)
   borders.append(border_list)
   #print(f"{sensor_x}:{sensor_y} => {beacon_x}:{beacon_y} || {mh_distance}")

max_mh = max(manhattens)


"""
my idea - check each border cell of each sensor diamond against each other sensor diamond

for all cells in set of cells that border diamonds and are inside the target square
   for each sensor
      if cell inside sensor range
         remove from set of cells
should be only 1 cell left
calc 4M * x + y of good cell (/beacon)
"""

# get all the border cells of all the sensors
candidates = set()

for b in borders:
   if len(b) > 0:
      for c in b:
         candidates.add(c)

winner = None

while len(candidates) > 1:
   cell = candidates.pop()
   discard = False
   for i, s in enumerate(sensors):
      sd = manhattens[i]

      cd =  mh(cell, s)

      if cd <= sd:
         discard = True

   if not discard:
      #candidates.add(cell)
      winner = cell
      break

#for c in candidates:
   #x, y = c
   #print(f"{x}:{y} | {4_000_000 * x + y}")
   #print(4_000_000 * x + y)

x, y = winner
#print(f"{x}:{y} | {4_000_000 * x + y}")
print(f"{4_000_000 * x + y}")
