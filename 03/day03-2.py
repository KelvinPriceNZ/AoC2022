#!/usr/bin/env python3

file=list()

def priority(char):
   if char.islower():
      return 1 + ord(char) - ord('a')
   if char.isupper():
      return 1 + 26 +  ord(char) - ord('A')

with open("./input.txt", "r") as f:
   file=f.read().splitlines()

sum = 0
for g in range(0,len(file),3):
   b = dict()

   for c in file[g]:
      b[c] = 1
      
   for c in file[g+1]:
      if b.get(c, 0) == 1:
         b[c] = 2
      
   for c in file[g+2]:
      if b.get(c, 0) == 2:
         b[c] = 3
      
   for c, _ in {k: v for k, v in b.items() if v == 3}.items():
      sum += priority(c)

print(sum)
