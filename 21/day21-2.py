#!/usr/bin/env python3
import sys
import math
import copy

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

monkeys = dict()

for line in lines:
   monkey, rule = line.split(":", 2)
   fields = rule.split()
   if len(fields) == 3:
      monkeys[monkey] = {
                           "opa": fields[0],
                           "op": fields[1],
                           "opb": fields[2],
                           "soln": None
                        }
   else:
      monkeys[monkey] = { "soln": int(fields[0]) }

monkeys["root"]["op"] = "=="

orig_monkeys = copy.deepcopy(monkeys)

def dfs(monkey):
   if monkeys[monkey]["soln"] is not None:
      return monkeys[monkey]["soln"]
   else:
      opa = dfs(monkeys[monkey]["opa"])
      monkeys[monkey]["opa"] = opa
      op = monkeys[monkey]["op"]
      opb = dfs(monkeys[monkey]["opb"])
      monkeys[monkey]["opb"] = opb
      soln = eval(f"({opa} {op} {opb})")
      monkeys[monkey]["soln"] = soln
      return soln

result = dfs("root")

lhs = monkeys["root"]["opa"]
rhs = monkeys["root"]["opb"]

guess = 335
d = int(pow(2,35))

#print(orig_monkeys["root"])
#print(f"{rhs:20} {lhs:20} {guess:20} {d:15}")

# Doing a binary search, I'm sure there's a better way
while not result:
   while lhs < rhs:
      guess -= d
      #print(f"{rhs:20} {lhs:20} {guess:20} {d:15} D")
      monkeys = copy.deepcopy(orig_monkeys)
      monkeys["humn"]["soln"] = guess
      result = dfs("root")
      lhs = monkeys["root"]["opa"]
      rhs = monkeys["root"]["opb"]
   d //= 2
   while lhs > rhs:
      guess += d
      #print(f"{rhs:20} {lhs:20} {guess:20} {d:15} U")
      monkeys = copy.deepcopy(orig_monkeys)
      monkeys["humn"]["soln"] = guess
      result = dfs("root")
      lhs = monkeys["root"]["opa"]
      rhs = monkeys["root"]["opb"]
   d //= 2

print(guess)
