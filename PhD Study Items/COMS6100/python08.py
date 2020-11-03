# python 08
import os

lines = []
fn = "filelist.txt"
f = open(fn,"r")
for l in f:
  lines.append(l.strip())
f.close()

newlist = []
for l in lines:
 os.system("cat " + l)
