#!/usr/bin/env python3
import math

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

s = (10,10)
rope = [ s, s, s, s, s, s, s, s, s, s ]
t_hist = { rope[-1] : 1 }

o = {
   "U": 1,
   "D": -1,
   "L": -1,
   "R": 1
}

for line in lines:
   cmd, n = line.split()
   n = int(n)

   h = rope[0]
   hx, hy = h

   for m in range(1,n+1):
      if cmd == "R": hx += 1
      if cmd == "L": hx -= 1
      if cmd == "U": hy += 1
      if cmd == "D": hy -= 1
         
      h = ( hx, hy )
      rope[0] = h

      for knot in range(1, len(rope)):
         p = rope[knot - 1]
         c = rope[knot]

         px, py = p
         cx, cy = c

         dx = px - cx
         dy = py - cy
         d = ( dx, dy )

         if d == (-2, -2): cx -= 1; cy -= 1
         if d == (-2, -1): cx -= 1; cy -= 1
         if d == (-2,  0): cx -= 1;
         if d == (-2,  1): cx -= 1; cy += 1
         if d == (-2,  2): cx -= 1; cy += 1

         if d == (-1, -2): cx -= 1; cy -= 1
         if d == (-1, -1): pass
         if d == (-1,  0): pass
         if d == (-1,  1): pass
         if d == (-1,  2): cx -= 1; cy += 1

         if d == ( 0, -2): cy -= 1
         if d == ( 0, -1): pass
         if d == ( 0,  0): pass
         if d == ( 0,  1): pass
         if d == ( 0,  2): cy += 1

         if d == ( 1, -2): cx += 1; cy -= 1
         if d == ( 1, -1): pass
         if d == ( 1,  0): pass
         if d == ( 1,  1): pass
         if d == ( 1,  2): cx += 1; cy += 1

         if d == ( 2, -2): cx += 1; cy -= 1
         if d == ( 2, -1): cx += 1; cy -= 1
         if d == ( 2,  0): cx += 1
         if d == ( 2,  1): cx += 1; cy += 1
         if d == ( 2,  2): cx += 1; cy += 1

         c = (cx ,cy)
         rope[knot] = c

      t_hist[rope[-1]] = 1


print(len(t_hist.keys()))
