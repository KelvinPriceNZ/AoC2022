#!/usr/bin/env python3

def calc_score(height, trees):
   max = -1
   total = 0
   for tree in trees:
      (h, _) = tree
      if h >= height:
         return total + 1
      total += 1

   return total

def product(nums):
   total = 1
   for n in nums:
      if n > 0: total *= n
   return total

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

grid = list()

for y, line in enumerate(lines):
   grid.append(list())
   for x, c in enumerate(line):
      t = (int(c), 0)
      grid[y].append(t)

side = len(grid)

for r, row in enumerate(grid):
   for c, tree in enumerate(row):
      ( height, score ) = tree
      scores = list()

      tract = []
      for w in range(c-1,-1,-1):
         tract.append(grid[r][w])
      scores.append(calc_score(height, tract))

      tract = []
      for e in range(c+1,side,1):
         tract.append(grid[r][e])
      scores.append(calc_score(height, tract))

      tract = []
      for n in range(r-1,-1,-1):
         tract.append(grid[n][c])
      scores.append(calc_score(height, tract))

      tract = []
      for s in range(r+1,side,1):
         tract.append(grid[s][c])
      scores.append(calc_score(height, tract))

      score = product(scores)
      grid[r][c] = ( height, score )

best = -1

for row in grid:
   for tree in row:
      ( height, score ) = tree
      if score > best:
         best = score

print(best)
