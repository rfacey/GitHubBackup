# python 09
import os

words = []
lines = []
fn = "161.txt"
f = open(fn,"r")
for l in f:
  words = l.strip().split()
  lines.append(words)
f.close()

for l in lines:
  print l
  for w in l:
     print w
