#!/usr/bin/env python3
import sys
#import curses
#from curses import wrapper

#w = curses.initscr()

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

cave = list()
for row in range(1_000):
   cave.append(list())
   for col in range(1_000):
      cave[row].append(".")

width = 180
x_offset = 500 - width // 2
y_offset = 0

def draw():
   for col in range(180):
      for row in range(50):
         w.addch(row, col,  cave[row + y_offset][col + x_offset])

   w.addstr(53,0, f"{blocked:5}")
   w.move(54,0)
   w.refresh()
   w.getch(55,0)

max_x = -1
max_y = -1
for line in lines:
   fields = line.split(" -> ")
   for field, coord in enumerate(fields[:-1]):
      from_x, from_y = eval(coord)
      dest_x, dest_y = eval(fields[field + 1])
      from_x = int(from_x)
      from_y = int(from_y)
      dest_x = int(dest_x)
      dest_y = int(dest_y)
      max_y = max([max_y, from_y, dest_y])
      max_x = max([max_x, from_x, dest_x])
      cave[from_y][from_x] = "#"
      cave[dest_y][dest_x] = "#"
      if from_x == dest_x:
         pos1 = min([from_y, dest_y])
         pos2 = max([from_y, dest_y])
         for y in range(pos1,pos2):
            cave[y][from_x] = "#"
      if from_y == dest_y:
         pos1 = min([from_x, dest_x])
         pos2 = max([from_x, dest_x])
         for x in range(pos1,pos2):
            cave[from_y][x] = "#"

cave[max_y + 2] = [ "#" for i in range(1000) ]
max_y += 2

blocked = 0
drop_more = True

cave[0][500]="+"
while drop_more:
   x, y = 500, 0
   #draw()
   while y < max_y:
      #w.addstr(52,0, f"X {x:3}:{y:3}")
      old_x = x
      old_y = y
      if cave[y+1][x] == ".":
         y += 1
      elif cave[y+1][x-1] == ".":
         y += 1
         x -= 1
      elif cave[y+1][x+1] == ".":
         y += 1
         x += 1
      else:
         #w.addstr(55,0, f"blocked at {x:3}:{y:3}")
         cave[y][x] = "@"
         blocked += 1
         if x == 500 and y == 0: drop_more = False
         break
      cave[y][x] = "o"
      cave[old_y][old_x] = "."

      y_offset = max([0,y -20])
   if y >= max_y:
      drop_more = False

#draw()
#w.getch(55,0)

#curses.endwin()

#print(max_x)
#print(max_y)
print(blocked)
