#!/usr/bin/env python3

class DirTree:

   def __init__(self, name):
      self.name = name
      self.size = 0
      self.files = list()
      self.dirs = dict()
      self.parent = None

   def get_size(self):
      total = 0
      for file in self.files:
         total += file.size
      for name, dir in self.dirs.items():
         total += dir.get_size()
      self.size = total
      return total

   def __repr__(self):
      me = ""
      for file in self.files:
         me += str(file) + "\n"
      for dir in self.dirs.values():
         me += f"{dir.name}: {dir.size}\n"
      return me

class File:

   def __init__(self, name, size):
      self.name = name
      self.size = size

   def __repr__(self):
      return f"{self.name}: {self.size}\n"

lines = list()

with open("./input.txt", "r") as f:
   lines=f.read().splitlines()

root = DirTree("/")
cwd="/"
for line in lines:
   fields = line.split()

   if fields[0] == "$":
      if fields[1] == "cd":
         if fields[2] == "/":
            cwd = "/"
            tree = root
         elif fields[2] == "..":
            nodes = cwd.split("/")[1:]
            nodes.pop()
            if len(nodes) == 0:
               cwd = "/"
            elif len(nodes) == 1:
               cwd = "/" + nodes[0]
            else:
               cwd = "/" + "/".join(nodes)
            if cwd == "/":
               tree = root
            else:
               tree = tree.parent
         else:
            if cwd[-1] != "/":
               cwd += "/"
            cwd += fields[2]
            parent_tree = tree
            tree = tree.dirs[fields[2]]
            #print(cwd)

   else:
      if fields[0] == "dir":
         name = fields[1]
         tree.dirs[name]=(DirTree(name))
         tree.dirs[name].parent=tree
         #print(f"adding dir {name} to {tree.name}")
      else:
         size = int(fields[0])
         name = fields[1]
         file = File(name, size)
         tree.files.append(file)
         #print(f"adding file {name} to {tree.name}")

#print("Files")
#for file in root.files:
   #print(file)

#print("Size")
for name, dir in root.dirs.items():
   dir.get_size()
root.get_size()

targets=list()
#print("Dirs")
def print_dirs(dirtree):
   for dir in dirtree.dirs.values():
      #print(dir)
      print_dirs(dir)
      if dir.size <= 100_000:
         targets.append(dir.size)

print_dirs(root)
#print(sum(targets))

fs_size=70000000
df_size=30000000

#print("====")
#print(root.size)
#print(fs_size - root.size)

targets=list()
def print_dirs(dirtree):
   for dir in dirtree.dirs.values():
      #print(dir)
      print_dirs(dir)
      #print(f"{fs_size} {fs_size - root.size} {fs_size - root.size + dir.size}")
      if fs_size - root.size + dir.size > df_size:
         targets.append(dir.size)

print_dirs(root)
#print(targets)
print(min(targets))
