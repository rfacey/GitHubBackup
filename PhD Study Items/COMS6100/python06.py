# python 06
# basic reading of a data file

lines = []
fn = "filelist.txt"
f = open(fn,"r")
for l in f:
  lines.append(l.strip())
f.close()

for l in lines:
  aa = l.split(".")
  print l, aa[0], len(aa), len(aa[0]), aa
