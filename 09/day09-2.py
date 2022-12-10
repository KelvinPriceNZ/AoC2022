#!/usr/bin/env python3
import math

s = (0,0)
rope = list()
rope_length = 10
for i in range(rope_length):
   rope.append(s)

tail_history = { rope[-1] : 1 }

""" Possible delta positions from current position
[ (-2,-2), (-2,-1), (-2, 0), (-2, 1), (-2, 2) ],
[ (-1,-2), (-1,-1), (-1, 0), (-1, 1), (-1, 2) ],
[ ( 0,-2), ( 0,-1), ( 0, 0), ( 0, 1), ( 0, 2) ],
[ ( 1,-2), ( 1,-1), ( 1, 0), ( 1, 1), ( 1, 2) ],
[ ( 2,-2), ( 2,-1), ( 2, 0), ( 2, 1), ( 2, 2) ]
"""

# Lookup table for move delta
move_table = [
   [ (-1,-1), (-1,-1), (-1, 0), (-1, 1), (-1, 1) ],
   [ (-1,-1), ( 0, 0), ( 0, 0), ( 0, 0), (-1, 1) ],
   [ ( 0,-1), ( 0, 0), ( 0, 0), ( 0, 0), ( 0, 1) ],
   [ ( 1,-1), ( 0, 0), ( 0, 0), ( 0, 0), ( 1, 1) ],
   [ ( 1,-1), ( 1,-1), ( 1, 0), ( 1, 1), ( 1, 1) ]
]

def calc_delta(prev, curr):
   px, py = prev
   cx, cy = curr

   dx = px - cx
   dy = py - cy

   return ( dx, dy )

def calc_move(m):
   mx, my = m

   mx += 2
   my += 2

   return move_table[mx][my]

def make_move(current, delta):
   fx, fy = current
   dx, dy = delta
   fx += dx
   fy += dy
   return (fx, fy)

cmd_delta = {
   "U": ( 0, 1),
   "D": ( 0,-1),
   "L": (-1, 0),
   "R": ( 1, 0)
}

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

for line in lines:
   cmd, n = line.split()
   n = int(n)

   # Move head one step at a time
   for m in range(1,n+1):
      rope[0] = make_move(rope[0], cmd_delta[cmd])

      # Make rest of rope adjust accordingly for each head move
      for knot in range(1, len(rope)):
         p = rope[knot - 1]
         c = rope[knot]

         rope[knot] = make_move(c, calc_move(calc_delta(p,c)))

      tail_history[rope[-1]] = 1

print(len(tail_history.keys()))
