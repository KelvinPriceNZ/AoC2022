#!/usr/bin/env python3

file=list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

count = 0
for line in lines:
   r1, r2 = line.split(',')
   b1, e1 = r1.split('-')
   b2, e2 = r2.split('-')

   flag = False
   if int(b1) >= int(b2) and int(b1) <= int(e2):
      flag = True

   if int(b2) >= int(b1) and int(b2) <= int(e1):
      flag = True

   if flag: count+=1

print(count)
