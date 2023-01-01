#!/usr/bin/env python3

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

def dfs(monkey):
   if monkeys[monkey]["soln"] is not None:
      return monkeys[monkey]["soln"]
   else:
      opa = dfs(monkeys[monkey]["opa"])
      monkeys[monkey]["opa"] = opa
      op = monkeys[monkey]["op"]
      if op == "/": op = "//"
      opb = dfs(monkeys[monkey]["opb"])
      monkeys[monkey]["opb"] = opb
      soln = eval(f"{opa} {op} {opb}")
      monkeys[monkey]["soln"] = soln
      return soln

print(dfs("root"))
