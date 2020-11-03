# python 05
# basic reading of a data file

lines = []
fn = "filelist.txt"
f = open(fn,"r")
for l in f:
  lines.append(l.strip())
f.close()

for l in lines:
  if l.find("2") <> -1:  # look for lines that have "2" in them
     print l
