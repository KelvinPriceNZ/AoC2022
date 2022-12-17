#!/usr/bin/env python3
import math
import sys
sys.setrecursionlimit(10_000)
import curses
from functools import cmp_to_key
from Node import Node
from collections import deque

w = curses.initscr()

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

route = list()
solution = list()
land_map = list()
min_steps = 500

start=None
finish=None

def draw():
   for x, row in enumerate(land_map):
      for y, col in enumerate(row):
         c = land_map[x][y].height
         if land_map[x][y].visited:
            c = "#"
         w.addch(x, y, c)
   w.refresh()

def neighbours(cell):
   col = cell.y
   row = cell.x

   rb = len(land_map[row]) - 1
   bb = len(land_map) - 1

   coords = list()

   for ox in [ 1, 0, -1 ]:
      if row + ox <  0: continue
      if row + ox > bb: continue
      for oy in [ -1, 0, 1 ]:
         if abs(ox) == 1 and abs(oy) == 1: continue
         if ox == 0 and oy == 0: continue
         if col + oy <  0: continue
         if col + oy > rb: continue

         x = row + ox
         y = col + oy

         coords.append(land_map[x][y])

   return coords

def cmp_v(a,b):
   ax, ay = a.x, a.y
   bx, by = b.x, b.y
   ex, ey = finish.x, finish.y
   mha = abs(ax-ex) + abs(ay-ey)
   mhb = abs(bx-ex) + abs(by-ey)
   if mha < mhb:
      return -1
   elif mha > mhb:
      return 1
   else:
      return 0
   
for x, line in enumerate(lines):
   land_map.append([])
   for y, c in enumerate(list(line)):
      land_map[x].append(Node(x,y,c))

for x, r in enumerate(land_map):
   for y, c in enumerate(r):
      if land_map[x][y].height == "S": start  = Node(x,y,c.height); land_map[x][y].height = chr(ord("a") - 1)
      if land_map[x][y].height == "E": finish = Node(x,y,c.height); land_map[x][y].height = chr(1 + ord("z"))

"""
 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as explored
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  w.parent := v
13                  Q.enqueue(w)
"""

open_queue = deque()

start.set_counter(0)
start.visited = True

open_queue.append(land_map[start.x][start.y])

draw()

counter = 0

while len(open_queue) > 0:
   counter += 1
   draw()
   cell = open_queue.popleft()
   w.addstr(52,0,str(cell))

   if cell == finish:
      break

   exits = neighbours(cell)

   for n in exits:
      w.addstr(53,0,str(n))
      if land_map[n.x][n.y].visited:
         continue

      w.addstr(54,0,f"C: {cell.height} N: {land_map[n.x][n.y].height}")
      if ord(land_map[n.x][n.y].height) - ord(cell.height) > 1:
         continue

      open_queue.append(land_map[n.x][n.y])

      land_map[n.x][n.y].visited = True
      land_map[n.x][n.y].set_counter(cell.counter + 1)
      draw()

w.getch()
curses.endwin()
print("OUT")

print(f"count: {counter}")
print(f"S: {start}")
print(f"E: {land_map[finish.x][finish.y]}")

print(solution)
print(min_steps)
print(finish)
