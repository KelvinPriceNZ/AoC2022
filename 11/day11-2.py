#!/usr/bin/env python3
import sys
import math

divisor = 3
rounds = 20
if len(sys.argv) == 3:
   divisor = int(sys.argv[1])
   rounds = int(sys.argv[2])

monkeys = list()

class Monkey:

   def __init__(self, id, worry_test, rule, t_target, f_target, stash):
      self.id = id
      self.stash = stash
      self.inspections = 0
      self.target = {
         True:  t_target,
         False: f_target
      }
      self.worry_test = worry_test
      self.rule = rule

   def turn(self):
      if len(self.stash) > 0:
         #print(f"{self.id} has {self.stash}")
         for thing in self.stash:
            self.inspections += 1

            a_or_b, new_thing = self.calc(thing)

            throw_to = self.target[a_or_b]

            to_monkey = monkeys[throw_to]

            to_monkey.catch(new_thing)
            #print(f"Throwing {new_thing} ({thing}) to monkey {throw_to}")

         self.stash = []

   def catch(self, thing):
      self.stash.append(thing)

   def calc(self, thing):
      old = thing
      #print(f"{self.id}|", end=" ")
      #print(old, end=" ")
      #print(self.rule, end=" ")
      worry = eval(self.rule)
      #print(f"= {worry}", end=" ")
      #worry //= 3
      #worry %= 96577
      worry %= 9699690
      #print(worry)
      divisible = worry % self.worry_test == 0
      #print(f"{worry} % {worry_test} {worry % worry_test} {divisible}")
      return ( divisible, worry )

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

monkey_id = 0
for line in lines:
   if line.startswith("Monkey"):
      continue

   if line != "" and line is not None:
      field, val = line.lstrip().split(":")
   else:
      monkey = Monkey(monkey_id, worry_test, rule, t_target, f_target, starting_items)
      monkeys.append(monkey)
      #print(f"Monkey: {len(monkeys)}")
      #print(f"Things: {starting_items}")
      #print(f"Rule: {rule}")
      #print(f"Test: {worry_test}")
      #print(f"T: {t_target}")
      #print(f"F: {f_target}")
      #print()
      monkey_id += 1

   if field == "Starting items":
      starting_items = list()
      for v in val.split(","):
         starting_items.append(int(v))

   if field == "Operation":
       rule = " ".join(val.split()[2:])

   if field == "Test":
      worry_test = int(val.split()[-1])

   if field == "If true":
      t_target = int(val.split()[-1])

   if field == "If false":
      f_target = int(val.split()[-1])

for round in range(rounds):
   #print(f"{round:6}")
   for monkey in monkeys:
      #print(f"{monkey.id:2}: {round:6} {monkey.inspections:7} {monkey.stash} : ({monkey.rule}) % {monkey.worry_test}")
      monkey.turn()

scores = list()

for monkey in monkeys:
   scores.append(monkey.inspections)

#print(rounds, end=" | ")
#print(scores, end=" | ")

#print(scores[0] * scores[-1], end=" | ")
scores.sort()

#print(scores)
print(scores[-1] * scores[-2])
