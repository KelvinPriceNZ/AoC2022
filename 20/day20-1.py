#!/usr/bin/env python3
import copy

class Row:

   def __init__(self, val, col, idx):
      self.val = val
      self.col = col
      self.idx = idx

   def __str__(self):
      return f"{self.val} : {self.col} : {self.idx}"

   def __repr__(self):
      return f"Row({self.val}, {self.col}, {self.idx})"

   def __eq__(self, rhs):
      eq = True
      eq &= self.val == rhs.val
      eq &= self.col == rhs.col
      eq &= self.idx == rhs.idx

      return eq

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

code = list()
col = 0

for line in lines:
   row = Row(int(line), col, col)
   code.append(row)
   col += 1

size = len(code)

def display(a_list):
   n_list = [ str(c.val) for c in sorted(a_list, key=lambda x: x.col) ]
   return ", ".join(n_list)

code2 = copy.deepcopy(code)

for n in range(size):
   col = code[n].col
   val = code[n].val
   idx = code[n].idx

   for i in range(size):
      b = code[i].col
      code2[b] = copy.deepcopy(code[i])
      code2[b].col = b

   filler = Row(-1,-1,-1)

   row = copy.deepcopy(code[n])

   pos = col + val

   pos += pos // size
   pos %= size

   if pos == 0: pos = -1

   code2.append(filler)
   code2.remove(row)
   row.col = pos
   code2.insert(pos, row)
   code2.remove(filler)

   for i in range(size):
      c = code2[i].idx
      code[c] = copy.deepcopy(code2[i])
      code[c].col = i

final = [ 0 for x in range(size) ]

offset = 0
for n in range(size):
   c = code[n].col
   final[c] = code[n].val
   if code[n].val == 0:
      offset = code[n].col

#print(*final)

x = (offset + 1000) % size
y = (offset + 2000) % size
z = (offset + 3000) % size

print(f"{x}:{y}:{z} | {final[x]} + {final[y]} + {final[z]} = {final[x] + final[y] + final[z]}")
