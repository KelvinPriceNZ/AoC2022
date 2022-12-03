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
for line in [x.strip() for x in file]:
   l = len(line)
   d = int(l/2)

   r1 = line[:d]
   r2 = line[d:]

   b = dict()

   for i in r1:
      b[i]=1

   for i in r2:
      if b.get(i,0) == 1:
         b[i]=2

   for c, _ in {k: v for k, v in b.items() if v == 2}.items():
      sum += priority(c)

print(sum)
