#!/usr/bin/env python3
import math
import re

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

min_x = math.inf
max_x = -math.inf

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

   #print(f"{sensor_x}:{sensor_y} => {beacon_x}:{beacon_y} || {mh_distance}")

max_mh = max(manhattens)

blocks = dict()
for s, sensor in enumerate(sensors):
   sx, sy = sensor
   mhd = manhattens[s]
   for x in range(sx - mhd, sx + mhd):
      if mh((x,2_000_000),sensor) <= manhattens[s]:
         if (x,2_000_000) not in beacons:
            blocks[(x,2_000_000)] = 1
            #print(f"Overlap at {x}:2_000_000")
         else:
            #print(f"B at {x}:2_000_000")
            pass
   
print(len(blocks.keys()))
