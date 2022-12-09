#!/usr/bin/env python3

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

grid = list()

for y, line in enumerate(lines):
   grid.append(list())
   for x, c in enumerate(line):
      t = (int(c), False)
      grid[y].append(t)

side = len(grid)

for x in range(side):
   max = -1
   for y in range(side):
      ( height, visible ) = grid[x][y]
      if height > max:
         max = height
         grid[x][y] = ( height, True )
      
for y in range(side):
   max = -1
   for x in range(side):
      ( height, visible ) = grid[x][y]
      if height > max:
         max = height
         grid[x][y] = ( height, True )
      
for x in reversed(range(side)):
   max = -1
   for y in reversed(range(side)):
      ( height, visible ) = grid[x][y]
      if height > max:
         max = height
         grid[x][y] = ( height, True )
      
for y in reversed(range(side)):
   max = -1
   for x in reversed(range(side)):
      ( height, visible ) = grid[x][y]
      if height > max:
         max = height
         grid[x][y] = ( height, True )
      

total = 0
for row in grid:
   for tree in row:
      ( height, visible ) = tree
      if visible:
         total += 1

print(total)
