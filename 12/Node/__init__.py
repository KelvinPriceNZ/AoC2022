class Node:
   def __init__(self, x, y, c):
      if type(x) != int: raise TypeError
      if type(y) != int: raise TypeError
      if type(c) != str: raise TypeError
      self.x = x
      self.y = y
      self.height = c
      self.counter = 0
      self.visited = False

   def __str__(self):
      return f"{self.x}:{self.y} {self.height} {self.visited} C:{self.counter}"

   def __eq__(self, rhs):
      return self.x == rhs.x and self.y == rhs.y

   def next_door(self, n):
      connected = False
      if self.x == n.x:
         if self.y == n.y + 1: connected = True
         if self.y == n.y - 1: connected = True
      if self.y == n.y:
         if self.x == n.x + 1: connected = True
         if self.x == n.x - 1: connected = True

      return connected

   def set_counter(self, val):
      self.counter = val

      return self.counter
