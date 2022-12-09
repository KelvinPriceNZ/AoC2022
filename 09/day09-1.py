#!/usr/bin/env python3

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

s = h = t = (0,0)
t_hist = { t : 1 }

for line in lines:
   cmd, n = line.split()
   n = int(n)
   ( hx, hy ) = h
   ( tx, ty ) = t

   for m in range(1,n+1):
      if cmd == "R": hx += 1
      if cmd == "L": hx -= 1
      if cmd == "U": hy += 1
      if cmd == "D": hy -= 1

      h = ( hx, hy )
      
      if hx - tx >  1 : tx += 1; ty = hy
      if hx - tx < -1 : tx -= 1; ty = hy
      if hy - ty >  1 : ty += 1; tx = hx
      if hy - ty < -1 : ty -= 1; tx = hx

      t = ( tx, ty )
      t_hist[t] = 1

print(len(t_hist.keys()))
