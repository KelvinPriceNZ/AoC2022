#!/usr/bin/env python3

file=list()

with open("./input.txt", "r") as f:
   file=f.read().splitlines()

RPS = {
         "A" : "R",
         "B" : "P",
         "C" : "S",
         "X" : "L",
         "Y" : "D",
         "Z" : "W"
      }

SCORE = {
            "R" : 1,
            "P" : 2,
            "S" : 3
         }

def Beats(them):
   if them == "R": return "P"
   if them == "P": return "S"
   if them == "S": return "R"

def Draws(them):
   return them

def Loses(them):
   if them == "R": return "S"
   if them == "P": return "R"
   if them == "S": return "P"

def Result(them, me):
   if them == "R" and me == "R": return 3
   if them == "R" and me == "P": return 6
   if them == "R" and me == "S": return 0
   if them == "P" and me == "R": return 0
   if them == "P" and me == "P": return 3
   if them == "P" and me == "S": return 6
   if them == "S" and me == "R": return 6
   if them == "S" and me == "P": return 0
   if them == "S" and me == "S": return 3

total_score = 0

for line in file:
   (elf, me) = line.split()
   elf = RPS[elf]
   me = RPS[me]
   if me == "W": me = Beats(elf)
   if me == "D": me = Draws(elf)
   if me == "L": me = Loses(elf)
   score = Result(elf, me) + SCORE[me]
   total_score += score


print(total_score)
