# python 07
# basic reading of a data file

lines = []
fn = "filelist.txt"
f = open(fn,"r")
for l in f:
  lines.append(l.strip())
f.close()

newlist = []
for l in lines:
  aa = l.split(".")
  newlist.append(aa)

