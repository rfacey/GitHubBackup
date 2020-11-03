# python 04
# basic reading of a data file

lines = []
fn = "filelist.txt"
f = open(fn,"r")
for l in f:
  lines.append(l.strip())
f.close()

for l in lines:
  print l
