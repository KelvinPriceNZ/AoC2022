#!/usr/bin/env python3
import math

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

pairs = list()
for line in lines:
   if line == "": continue
   in_list = eval(line)
   pairs.append(in_list)

left_list  = [x for i, x in enumerate(pairs) if i % 2 == 0]
right_list = [x for i, x in enumerate(pairs) if i % 2 == 1]

def compare(l, r, depth = 0):
   in_order = True

   print(f"{l} Vs {r} : {depth}")

   if type(l) != list: l = [ l ]
   if type(r) != list: r = [ r ]

   for i, lv in enumerate(l):
      if i == len(r):
         # r is shorter than l, in_order = False
         in_order = False
         break
      rv = r[i]
      if type(lv) == int and type(rv) == int:
         if lv == rv: continue
         if lv < rv:
            in_order = True
         else:
            in_order = False
         break

      if type(lv) == int: lv = [ lv ]
      if type(rv) == int: rv = [ rv ]

      if type(lv) == list and type(rv) == list:
         if len(lv) == 0 and len(rv) == 0: continue
         in_order &= compare(lv,rv, depth + 1)
         break

   return in_order

sum = 0
for p in range(len(left_list)):
   left = left_list[p]
   right = right_list[p]

   if compare(left, right):
      print(f"T {p+1}")
      index = p + 1
      sum += index
   else:
      print(f"F {p+1}")

print(f"Sum: {sum}")
